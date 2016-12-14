from django.shortcuts import render
from django.http import HttpResponse
from main.forms import ImageUploadForm, LoginForm, SignUpForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_backends


def demo(request):
    form = ImageUploadForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS,"Form uploaded successfully")
            files = request.FILES.getlist('images')
            for file in files:
                print file
            return render(request, 'demo.html', {
                'title': 'Hypothizer Labs',
                'form': form
            })
        else:
            messages.add_message(request, messages.WARNING, "Please select a file")
            print "Handle invalid post"
            return render(request, 'demo.html', {
                'title': 'Hypothizer Labs',
                'form': form
            })
    else:
        print "handle get"
        return render(request, 'demo.html', {
            'title': 'Hypothizer Labs',
            'form': form
        })


def index(request):
    return render(request, 'index_grey.html')


def about(request):
    return render(request, 'index_grey.html')


def login_signup(request):
    login_form = LoginForm(request.POST or None)
    signup_form = SignUpForm(request.POST or None)
    if "Login" in request.POST:
        print('Login form submitted')
        if login_form.is_valid():
            print('valid login form')
            messages.add_message(request, messages.SUCCESS, "Login Successfull")
            return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
        else:
            print('INVALID login form')
            messages.add_message(request, messages.WARNING, "Login Failed")
            return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
    if "Signup" in request.POST:
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
                return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
        else:
            print('INVALID signup form')
            messages.add_message(request, messages.WARNING, "Signup Failed")
            return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
    else:
        print('handle get')
        return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})




