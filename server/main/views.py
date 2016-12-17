from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.forms import ImageUploadForm, LoginForm, SignUpForm, FolderUploadForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_backends
import os
import sys
import datetime
from hypothizer_lab.settings import UPLOAD_TO
import subprocess

def index(request):
    return render(request, 'index_grey.html')


def logout(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    auth.logout(request)
    return HttpResponseRedirect('/')


def login_signup(request):
    login_form = LoginForm(request.POST or None)
    signup_form = SignUpForm(request.POST or None)
    if "Login" in request.POST:
        logout(request)
        print('Login form submitted')
        if login_form.is_valid():
            print('valid login form')
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            try:
                user = authenticate(username=email, password=password)
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, "Login successful")
                return HttpResponseRedirect('/demo')
                # return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
            except:
                messages.add_message(request, messages.WARNING, "Username or password wrong")
                return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
        else:
            print('INVALID login form')
            messages.add_message(request, messages.WARNING, "Login Failed")
            return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
    if "Signup" in request.POST:
        logout(request)
        print('Signup form submitted')
        if signup_form.is_valid():
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password_s']

            if User.objects.filter(email=email).exists():
                messages.add_message(request, messages.WARNING, "Email Already Exist")
                return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
            else:
                user = User.objects.create(username=email)
                user.email = email
                user.set_password(password)
                user.is_staff = False
                user.is_active = True
                user.is_superuser = False
                user.save()
                user = authenticate(username=email, password=password)
                auth.login(request, user)
                print('valid signup form')
                messages.add_message(request, messages.SUCCESS, "Signup Successfull")
                return HttpResponseRedirect('/demo')
                # return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
        else:
            print('INVALID signup form')
            messages.add_message(request, messages.WARNING, "Enter a valid email address")
            return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
    else:
        print('handle get')
        return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})


def demo(request):
    single_image_form = ImageUploadForm(request.POST, request.FILES or None)
    folder_form = FolderUploadForm(request.POST, request.FILES or None)
    if "Upload_image" in request.POST:
        if single_image_form.is_valid():
            print('in single form')
            file = single_image_form.cleaned_data['image']
            print(file)
            uploaded_img_folder = os.path.join(UPLOAD_TO, "anonymous")
            if not os.path.exists(uploaded_img_folder):
                os.makedirs(uploaded_img_folder)
            if ".png" in file.name or ".jpg" in file.name:
                dest = None
                for chunk in file.chunks():
                    dest = open(os.path.join(uploaded_img_folder, file.name), "wb+")
                    dest.write(chunk)
                dest.close()
                messages.add_message(request, messages.SUCCESS, "Image uploaded successfully")
            else:
                messages.add_message(request, messages.WARNING, "Please select an image with png or jpg format")
            return render(request, 'demo.html', {
                'title': 'Hypothizer Labs',
                'single_image_form': single_image_form,
                'folder_form': folder_form
            })
        else:
            messages.add_message(request, messages.WARNING, "Please select a file")
            print "Handle invalid post"
            return render(request, 'demo.html', {
                'title': 'Hypothizer Labs',
                'single_image_form': single_image_form,
                'folder_form': folder_form
            })
    elif "Upload_folder" in request.POST:
        print('In folder form')
        subprocess.call("ls > new.txt", shell=True)

        if folder_form.is_valid():
            messages.add_message(request, messages.SUCCESS, "Form uploaded successfully")
            files = request.FILES.getlist('image_folder')
            uploaded_img_folder = os.path.join(UPLOAD_TO, request.user.username)
            if not os.path.exists(uploaded_img_folder):
                os.makedirs(uploaded_img_folder)

            print files
            for file in files:
                for chunk in file.chunks():
                    if ".png" in file.name:
                        dest = open(os.path.join(uploaded_img_folder, file.name), "wb+")
                        dest.write(chunk)
                dest.close()
            return render(request, 'demo.html', {
                'title': 'Hypothizer Labs',
                'single_image_form': single_image_form,
                'folder_form': folder_form
            })
        else:
            messages.add_message(request, messages.WARNING, "Please select a file")
            print "Handle invalid post"
            return render(request, 'demo.html', {
                'title': 'Hypothizer Labs',
                'single_image_form': single_image_form,
                'folder_form': folder_form
            })
    else:
        print('Got in else')
        return render(request, 'demo.html', {
            'title': 'Hypothizer Labs',
            'single_image_form': single_image_form,
            'folder_form': folder_form
        })


def result(request):
    return render(request, 'result.html')



