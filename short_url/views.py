from django.shortcuts import render
from django.http import HttpResponse
import string
import random
from short_url.models import url_mapping


def index(request):
    if request.method == "GET":
        return render(request, 'short_url/index.html')
    else:
        post_data = request.POST.copy()
        print(post_data)
        data = dict()

        data["validity"] = post_data["validity"]

        gen_url = id_generator()
        data["genrated_url"] = gen_url

        url_mapping_instance = url_mapping(short_url=gen_url, long_url=post_data["original_url"],
                                           ttl=post_data["validity"])
        url_mapping_instance.save()

        return render(request, 'short_url/index.html', data)


def id_generator(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
