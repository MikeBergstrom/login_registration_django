# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile('^[^0-9]+$')


class UserManager(models.Manager):
    def register(self, data):
        errors =[]
        useremail = ""
        if len(data['first']) < 2:
            errors.append('First name must be at least 2 characters')
            print errors
            pass
        if len(data['last']) < 2:
            errors.append('Last name must be at least 2 characters')
            print errors
            pass
        if not NAME_REGEX.match(data['first']):
            errors.append('First name must be letters only')
            pass
        if not NAME_REGEX.match(data['last']):
            errors.append('Last name must be letters only')
            pass
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Email not in valid format')
            print "email match"
            pass
        # elif birth >= datetime.datetime.now()
        if data['password'] != data['confirm']:
            errors.append('Passwords do not match')
            pass
        if len(data['password']) < 8:
            errors.append('Password must be at least 8 characters')
            pass
        if User.objects.filter(email=data['email']).exists():
            errors.append('This email is already registered')
            pass
        if errors:
            return{'errors': errors}
        else:
            print "successful register"
            useremail = data['email']
            return{"useremail": data['email']}


    def login(self, data):
        errors = []
        if not User.objects.filter(email=data['email']).exists():
            errors.append('Email is not recognized')
            return{'errors':errors}
        else:
            user = User.objects.get(email=data['email'])
            print "in else statement"
            print user.password
            if user.password != password:
                errors.append('Incorrect Password')
            else:
                return{'first':user.first_name}


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
