# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'login/index.html')

def login(request):
    user= User.objects.login(request.POST['email'], request.POST['password'])
    if 'first' in user:
        request.session['first'] = user['first']
        request.session['status'] = "logged in"
        return render(request, 'login/success.html')
    elif 'errors' in user:
        request.session['logerrors']=user['errors'][0]
        return redirect('/')

def register(request):
    user = User.objects.register(request.POST['first'],request.POST['last'],request.POST['email'], request.POST['password'], request.POST['confirm'] )
    if 'useremail' in user:
        print "success"
        request.session['first']=request.POST['first']
        request.session['status']="registered"
        User.objects.create(first_name=request.POST['first'], last_name=request.POST['last'], email=request.POST['email'], password=request.POST['password'])
        return render(request, 'login/success.html')
    elif 'errors' in user:
        request.session['errors']=user['errors'][0]
        print "failure"
        print user['errors'][0]
        return redirect('/')
    
# Create your views here.
