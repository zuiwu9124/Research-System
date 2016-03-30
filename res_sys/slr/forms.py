# -*- coding:utf-8 -*-
from django import forms
from slr.models import *
from django.forms import widgets

class AddProject(forms.Form):
	project_id = forms.CharField(
		 required=False, label='project_id', max_length=30, widget=forms.TextInput(
            attrs={'type': 'text', 'class':'width-6'}))
	project_title = forms.CharField(
		 required=False, label='project_title', max_length=30,widget=forms.TextInput(
            attrs={'type': 'text', 'class':'width-6'}))	
	project_objective = forms.CharField(
		 required=False, label='project_objective', max_length=400,widget=forms.TextInput(
            attrs={'type': 'text', 'class':'width-6'}))	
