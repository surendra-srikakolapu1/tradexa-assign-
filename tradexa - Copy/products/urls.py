from django.urls import path
from .views import *
from products import views
from .urls import *

from django.contrib.auth.decorators import login_required


urlpatterns = [

     path('', views.homepage),

]
