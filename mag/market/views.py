from django.http import HttpResponseRedirect
from django.shortcuts import render


def welcome(request):
    if request.user.is_anonymous:
        HttpResponseRedirect('/login')
    else:
        HttpResponseRedirect('/home')