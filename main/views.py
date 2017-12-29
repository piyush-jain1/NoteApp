from django.contrib.auth.models import User
from django.core.mail import mail_admins
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.views.generic import View
from django.db import IntegrityError
from django.shortcuts import render_to_response

# from django.contrib.sites import requests


def user_signup(request):
    response_data = {}
    if request.method == "POST" and request.is_ajax:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        user_password = request.POST['password']
        full_name = name.split(' ')
        first_name = full_name[0]
        try:
            last_name = full_name[1]
        except:
            last_name = " "
        user_username = name.replace(" ", "").lower()
        print(user_username)
        try:
            temp1 = User.objects.get(email=email)
        except User.DoesNotExist:
            temp1 = None
        if temp1 is not None:
            response_data['register'] = "Failure_email"
            print(response_data)
            return HttpResponse(JsonResponse(response_data))
        try:
            temp2 = User.objects.get(phone=phone)
        except User.DoesNotExist:
            temp2 = None
        if temp2 is not None:
            response_data['register'] = "Failure_phone"
            print(response_data)
            return HttpResponse(JsonResponse(response_data))
        new_user = User.objects.create(username=user_username, email=email, first_name=first_name, last_name=last_name, phone=phone)
        new_user.save()
        new_user.set_password(user_password)
        new_user.is_active = True
        new_user.save()
        log_user = authenticate(username=user_username, password=user_password)
        if log_user is not None:
            login(request, log_user)
        response_data['register'] = "Success"
        message = "Hi Admin! New user "+ str(new_user.get_full_name()) +" has registered with you."
        if response_data['register'] == "Success":
            mail_admins(subject=str(new_user.id)+" new user registration!", message=message, fail_silently=False)
        response_data['phone'] = phone
        print(response_data)
        return HttpResponse(JsonResponse(response_data))

def user_login(request):
    username = password = ''
    response_data = {}
    if request.POST and request.is_ajax:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response_data = {'login' : "Success", 'username': username }
            else:
                response_data = {'user': "nouser"}
        else:
            # username = password = ''
            response_data = {'user': "password wrong"}
    else:
        response_data = {'login': "Failed"}
    return HttpResponse(JsonResponse(response_data))

def user_home(request):
    return render(request, 'main/home.html')