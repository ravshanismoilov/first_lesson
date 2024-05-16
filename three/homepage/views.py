from django.shortcuts import render
from django.http import HttpResponse


def get_info(request):
    return HttpResponse('I am from Uzbekistan, my name is Laziz')