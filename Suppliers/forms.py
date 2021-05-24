from django import forms
from django.forms import fields

from .models import Tbbeneficiarios

class TbbeneficiariosModelForm(forms.ModelForm):

    class Meta:
        model = Tbbeneficiarios
        fields = '__all__'