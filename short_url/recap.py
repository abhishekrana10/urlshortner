from django import forms
from short_url.models import recap
from short_url import config, utility



class recapForm(forms.ModelForm):
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
        super(recapForm, self).__init__(*args, **kwargs)

    class Meta:
        model = recap
        fields = ('short_url','ttl',)



