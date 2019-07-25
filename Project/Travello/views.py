from django.shortcuts import render
from .models import Destination

# Create your views here.
def Travel(request):
    dests = Destination.objects.all
    return render(request,'index.html',{'dests':dests})
