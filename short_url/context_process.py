from django.conf import settings # import the settings file

def site_name(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'site_name': settings.SITE_NAME}