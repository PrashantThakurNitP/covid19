from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db import IntegrityError
from .models import covidcasesModel
from django.shortcuts import render,redirect, get_object_or_404
#import django form

from django.utils import timezone






# Create your views here.

def home(request):

        cases=covidcasesModel.objects.all()#if we apply .all then for person everyon to do list will be shown


        #return render(request,"posts/feeds.html",{"case":feed})

       
        return render(request,"cases/home.html",{"home":"covidcases",'cases':cases})
 