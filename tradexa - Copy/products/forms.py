from django import forms
from .models import *



class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name' , 'weight' , 'price' , 'image']

