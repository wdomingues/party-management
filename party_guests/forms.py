from django import forms
from .models import Guest

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'email', 'cellphone','companion_qty', 
                  'companion_names', 'confirmed_1','confirmed_2','confirmed_3']