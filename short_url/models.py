from django.db import models
#from jsonfield import JSONField
#from django import forms

#from django.forms import ModelForm
#from short_url import config, utility
#from django import requests

class url_mapping(models.Model):
    short_url = models.CharField(max_length=8, primary_key=True)
    long_url = models.CharField(max_length=200)
    ttl = models.IntegerField()
    added = models.IntegerField()


class Short_url_info(models.Model):
    short_code = models.ForeignKey(url_mapping, on_delete=models.CASCADE)
    hits = models.IntegerField()


class deleted_url(models.Model):
    deleted_entry = models.CharField(max_length=8)


class recap(models.Model):
    short_url = models.CharField(max_length=8, primary_key=True)
    ttl = models.IntegerField()