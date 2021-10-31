from django.shortcuts import render , get_object_or_404
from .models import Business, ClientService, Configuration
def infos(request):
    business = Business.objects.all().last()
    sav = ClientService.objects.all()[:4]
    configuration = Configuration.get_solo()
    context = {
            'business' : business,
            'config' : configuration,
            'sav' : sav
        }
    return context
    

