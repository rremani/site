from django.shortcuts import render
from django.http import HttpResponse
from main.forms import ImageUploadForm, LoginForm, SignUpForm
from django.contrib import messages


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
    if request.method == 'POST':
        if login_form.is_valid():
            print('valid login form')
            return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
        else:
            print('INVALID login form')
            return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})
    else:
        print('handle get')
        return render(request, 'signup_login.html', {'login_form': login_form, 'signup_form': signup_form})




