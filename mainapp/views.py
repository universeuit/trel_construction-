from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    slider_objects = Slidermodel.objects.all()

    we_offers = Weoffer.objects.all()

    galleries = Gallery.objects.all()

    projects = Project.objects.all()

    ourteams = Ourteam.objects.all()

    latesnewss = Latesnews.objects.all()

    latesnewssimages = Latesnews.objects.all().values('image','id')
    print(latesnewssimages)


    context = {
        'slider_objects':slider_objects,
        'we_offers':we_offers,
        'galleries':galleries,
        'projects':projects,
        'ourteams':ourteams,
        'latesnewss':latesnewss,
        'latesnewssimages':latesnewssimages,
    }

    return render(request, 'index.html',context)


