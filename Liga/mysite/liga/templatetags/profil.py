#-*- coding: utf-8 -*-
from django import template
import datetime
from django.template.defaultfilters import stringfilter
from django.forms import ModelForm
from mysite.liga.models import Player

#class ProfilForm(forms.Form):
#        name = forms.CharField(label='Imię', max_length=15,required=True,)
#        surname = forms.CharField(label='Nazwisko',max_length=30,required=True)
#        pesel = forms.CharField(label='PESEL',max_length=11, required=True)
#        date = forms.DateField(label='Data urodzin',input_formats='%d-%m-%Y',required=True)
#        address = forms.CharField(label='Adres',max_length=50,required=False)
#        city = forms.CharField(label='Miasto',max_length=30,required=False)
#        isCapitan = forms.BooleanField(required=False)

class ProfilForm(ModelForm):
        class Meta:
                model = Player
                fields = ('name','surname','pesel','dateOfBrith','city','address','iscaptain')


