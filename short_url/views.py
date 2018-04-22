from django.shortcuts import render
from django.http import HttpResponse
from .recap import recapForm
import string
import random
from short_url.models import url_mapping, deleted_url, url_stats
import time, datetime
import httpagentparser
from short_url.utility import *
import requests, json
from urllib.request import urlopen
from django.db.models import Count


def index(request):
    if request.method == "GET":
        return render(request, 'short_url/index.html')

    else:
        post_data = request.POST.copy()
        form = recapForm(post_data, request=request)
        print(post_data)
        data = dict()
        data["is_response"] = True
        data["long_url"]=post_data["original_url"]
        data["validity"] = post_data["validity"]
        dt = datetime.datetime.today()
        time_now = int(time.mktime(dt.timetuple()))

        gen_url = id_generator()
        data["genrated_url"] = "http://localhost:8000/"+gen_url

        url_mapping_instance = url_mapping(short_url=gen_url, long_url=post_data["original_url"],
                                           ttl=post_data["validity"], added=time_now)
        url_mapping_instance.save()
        return render(request, 'short_url/index.html', data)


def id_generator(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))


def page_redirect(request, code):
    if request.method == "GET":
        print (code)
        print ("check")
        data = dict()
        flag = dict()
        ua = request.META['HTTP_USER_AGENT']
        ua_info = (httpagentparser.detect(ua))
        browser = ua_info['browser']['name']
        ip = utility.get_client_ip(request)
        if ip == '127.0.0.1':
            ip = urlopen('http://ip.42.pl/raw').read()
            s_ip=ip.decode()
        url = 'http://ip-api.com/json/' + s_ip
        r = requests.get(url)
        js = r.json()
        country = js['country']
        print(country)

        try:
            info = url_mapping.objects.get(short_url=code)
            data["long_url"] = info.long_url
            print("errorchecking"+info.short_url)
            if info.long_url.startswith('http://') or info.long_url.startswith('https://'):
                pass
            else:
                info.long_url = "http://" + info.long_url
            if info and info.ttl == -1:
                data["ttl"]=-1
                dt = datetime.datetime.today()
                hit_time = int(time.mktime(dt.timetuple()))
                url_stats_instance = url_stats(short_url=code, browser=browser, country=country, hit_time=hit_time)
                url_stats_instance.save()
                return render(request, 'short_url/page_redirect.html', data)
            elif info and info.ttl!=-1:
                data["long_url"] = info.long_url
                data["ttl"] = info.ttl
                dt = datetime.datetime.today()
                hit_time = int(time.mktime(dt.timetuple()))
                url_stats_instance = url_stats(short_url=info.short_url, browser=browser, country=country, hit_time=hit_time)
                url_stats_instance.save()
                return render(request, 'short_url/page_redirect.html', data)
        except Exception as e:
            print(e)
            try:
                if deleted_url.objects.get(deleted_entry=code):
                    flag["value"] = 1
                    return render(request, 'short_url/delete_redirect.html', flag)
            except Exception as e1:
                print(e1)
                flag["value"] = 0
                return render(request, 'short_url/delete_redirect.html', flag)


def error_404(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'short_url/error_404.html', data)

def stats(request):
    if request.method == "GET":
        return render(request, 'short_url/stats.html')
    else:
        post_data = request.POST.copy()
        data = dict()
        data['post_or_not'] = 1
        data["shortcode"] = post_data['entered_url']
        data["hits"] = url_stats.objects.filter(short_url=data['shortcode']).count()
        browser_count_list = url_stats.objects.filter(short_url=data['shortcode']).values('browser').annotate(total=Count('browser'))
        print(browser_count_list)
        data['bro_count'] = browser_count_list
        country_count_list = url_stats.objects.filter(short_url=data['shortcode']).values('country').annotate(total=Count('country'))
        data['country_count'] = country_count_list
        return render(request, 'short_url/stats.html', data)

        
    


