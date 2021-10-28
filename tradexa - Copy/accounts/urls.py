from django.urls import path
from accounts import views
from .urls import *

from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('accounts/register/',views.register,name='register')

]