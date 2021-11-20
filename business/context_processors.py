from django.contrib.admin.decorators import action
from django.shortcuts import render , get_object_or_404
from .models import Business, ClientService, Configuration, SEO, Realisation
def infos(request):
    business = Business.objects.all().last()
    sav = ClientService.objects.all()[:4]
    realisations = Realisation.objects.filter(actif=True)
    configuration = Configuration.get_solo()
    balises = SEO.objects.filter(actif=True, only_home_page=False)
    context = {
            'business' : business,
            'config' : configuration,
            'sav' : sav,
            'balises' : balises,
            'realisations' : realisations
        }
    return context
    

