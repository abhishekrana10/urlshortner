from django.shortcuts import render
from django.http import HttpResponse
import string
import random
from short_url.models import url_mapping, deleted_url
import datetime
import time


def index(request):
    if request.method == "GET":
        return render(request, 'short_url/index.html')
    else:
        post_data = request.POST.copy()
        print(post_data)
        data = dict()
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
        try:
            info = url_mapping.objects.get(short_url=code)
            if info.long_url.startswith('http://') or info.long_url.startswith('https://'):
                pass
            else:
                info.long_url = "http://" + info.long_url
            data["long_url"] = info.long_url
            if info and info.ttl == -1:
                data["ttl"]=-1
                return render(request, 'short_url/page_redirect.html', data)
            elif info and info.ttl!=-1:
                data["long_url"] = info.long_url
                data["ttl"] = info.ttl
                return render(request, 'short_url/page_redirect.html', data)
        except:
            try:
                if deleted_url.objects.get(deleted_entry=code):
                    flag["value"] = 1
                    return render(request, 'short_url/delete_redirect.html', flag)
            except:
                flag["value"] = 0
                return render(request, 'short_url/delete_redirect.html', flag)



