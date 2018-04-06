from django.db import models
#from jsonfield import JSONField

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

