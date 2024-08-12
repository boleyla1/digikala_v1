from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    Slider_Item = SliderItem.objects.all()
    return render(request, 'main/index.html', {'Slider_Item': Slider_Item })
