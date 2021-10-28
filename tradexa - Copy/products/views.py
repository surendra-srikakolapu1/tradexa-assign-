from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from django.contrib.auth.models import User,auth

@login_required
def homepage(request):

    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductModelForm()
            return redirect("/")

    else:
        form = ProductModelForm()
        result = Product.objects.all()


    return render(request,'index.html' ,{'form':form , 'allproducts':result})