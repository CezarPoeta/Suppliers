from django import forms
from django.db import models
from django.db.models import fields
from .models import Tbbeneficiarios


class BeneficiariosModelForm(forms.ModelForm):

    class Meta:
        model = Tbbeneficiarios
        fields = '__all__'