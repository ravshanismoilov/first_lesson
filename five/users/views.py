from django.shortcuts import render

# Create your views here.

def Bookname(request):
    return render(request, 'home.html')