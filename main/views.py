from . import models
from acct.models import Profile
from .forms import ContactForm, QuoteForm
from django.shortcuts import render, redirect
from project.utils import query_all_db, filter_query_db

def home_view(request):
    context = {
        'name':'home', 
        'service':query_all_db(models.Service),
    }
    return render(request, 'main/index.html', context)

def about_view(request):
    context = {
        'name':'about',
        'team':filter_query_db(Profile, team_member=True),
    }
    return render(request, 'main/about.html', context)

def service_view(request):
    context = {'name':'service'}
    return render(request, 'main/services.html', context)

def pricing_view(request):
    context = {'name':'pricing'}
    return render(request, 'main/pricing.html', context)

def member_view(request):
    context = {
        'name':'member',
        'team':filter_query_db(Profile, team_member=True),
    }
    return render(request, 'main/team.html', context)

def contact_view(request):
    context = {'name':'contact'}
    if request.method == 'POST':
        contact = ContactForm(data=request.POST)
        if contact.is_valid():
            contact.save()
            return redirect('home')
    else:
        return render(request, 'main/contact.html', context)

def quote_view(request):
    context = {'name':'quote'}
    if request.method == 'POST':
        quote = QuoteForm(data=request.POST)
        if quote.is_valid():
            quote.save()
            return redirect('home')
    else:
        return render(request, 'main/get-a-quote.html', context)
