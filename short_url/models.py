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


""" class recapForm(ModelForm):
    class Meta:
        model = recap

        def clean(self):
            ca = self.request.POST["g-recaptcha-response"]
            url = "https://www.google.com/recaptcha/api/siteverify"
            params = {
                'secret': config.RECAPTCHA_SECRET_KEY,
                'response': ca,
                'remoteip': utility.get_client_ip(self.request)
            }
            verify_rs = requests.get(url, params=params, verify=True)
            verify_rs = verify_rs.json()
            status = verify_rs.get("success", False)
            if not status:
                raise forms.ValidationError(
                    _('Captcha Validation Failed.'),
                    code='invalid',
                )
        def __init__(self, *args, **kwargs):
            self.request = kwargs.pop('request', None)
            super(recapForm, self).__init__(*args, **kwargs) """

