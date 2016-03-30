# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from slr import forms_dao,vo_dao
from slr.forms import *

def index_form(request):     
    return render_to_response('index.html')

def manage_project_form(request):
	if 'add' in request.POST:
		form = AddProject(request.POST)
		if form.is_valid():
			forms_dao.add_project(form,request)
			return HttpResponseRedirect('/my_project_list/')
	else:
		form = forms_dao.add_project_form()
	return render_to_response('manageproject.html',
								 {'form':form,},
								 context_instance=RequestContext(request))

def my_project_list(request):
	project_list = vo_dao.my_project_list()
	return render_to_response('my_project_list.html',
							 {'project_list':project_list})