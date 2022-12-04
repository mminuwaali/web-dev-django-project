from django.contrib.messages import success, error
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        user = authenticate(**request.POST)
        if user:
            profile = ProfileForm({'user':user}, request.FILES)
            if profile.is_valid():
                profile.save()
                success(request, 'Account created successfully')
                return redirect('home')
        else:
            error(request, "There was an error creating account")
    else:
        return render(request, 'acct/register.html')
