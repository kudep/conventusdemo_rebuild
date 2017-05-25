from django.shortcuts import render
from django.contrib import auth

# Create your views here.


def home(request):
    args = dict()
    args['username'] = auth.get_user(request).username
    return render(request, 'home/home.html', args)


def contacts(request):
    args = dict()
    args['username'] = auth.get_user(request).username
    return render(request, 'home/contacts.html', args)


def about(request):
    args = dict()
    args['username'] = auth.get_user(request).username
    return render(request, 'home/about.html', args)
