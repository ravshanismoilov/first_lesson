from django.shortcuts import render
from django.http import HttpResponse


def get_age(request):
    return HttpResponse('I am 18 years old')
