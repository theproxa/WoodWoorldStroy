from django import forms
from .models import Catalog

class Catalog_Form(forms.ModelForm):
    
    class Meta:
        model = Catalog
        fields = ['kind','product_len','thickness','width','material','image']