from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse
from .models import *
from .views import *

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User,auth


# Create your views here.

def register(request):
    form=UserCreationForm
    if request.method=='POST':
        regForm=UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered.')
    return render(request,'registration/register.html',{'form':form})