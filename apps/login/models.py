# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile('^[^0-9]+$')


class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_password):
        if len(first_name) < 2:
            return{'errors':['First name must be at least 2 characters']}
        elif  len(first_name)==0 | len(last_name)==0 | len(email)==0 | len(password)==0 |len(confirm_password)==0:
            return{'errors':['All fields are required']}
        elif len(last_name) < 2:
            return{'errors':['Last name must be at least 2 characters']}
        elif not NAME_REGEX.match(first_name):
            return{'errors':['First name must be letters only']}
        elif not NAME_REGEX.match(last_name):
            return{'errors':['Last name must be letters only']}
        elif not EMAIL_REGEX.match(email):
            return{'errors':['Email not in valid format']}
        elif password != confirm_password:
            return{'errors': ['Passwords do not match']}
        elif len(password) < 8:
            return{'errors':['Password must be at least 8 characters']}
        elif User.objects.filter(email=email).exists():
            return{'errors':['This email is already registered']}
        else:
            print "successful register"
            return{'useremail': email}

    def login(self, email, password):
        if not User.objects.filter(email=email).exists():
            return{'errors':['Email address not found in system']}
        else:
            user = User.objects.get(email=email)
            print "in else statement"
            print user.password
            if user.password != password:
                return{'errors':['Incorrect Password']}
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
