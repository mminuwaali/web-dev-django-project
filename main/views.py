from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'main/home.html')