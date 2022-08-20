from django import forms
from.models import *

class AddCarForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ('brand','model','year', 'image')
