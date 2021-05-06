from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from Product.models import *
# Create your views here.


def Home(request):
    settings = Setting.objects.get(id=1)
    slider_image = SliderImage.objects.all().order_by('-id')
    right_image = RightImage.objects.all().order_by('-id')[:2]
    context = {'settings': settings,
               'slider_image': slider_image, 'right_image': right_image}
    return render(request, 'EcomApp/home.html', context)
