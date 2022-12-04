from django.contrib.messages import success, error
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        user = UserForm(data=request.POST)
        # user = User.objects.create_user(data=request.POST)
        user.save()
        return redirect('home')
        # if user.is_valid():
        #     user.save()
        #     # profile = ProfileForm({'user':user}, request.FILES)
        #     # if profile.is_valid():
        #     #     profile.save()
        #     #     success(request, 'Account created successfully')
        #     return redirect('home')
        # else:
        #     error(request, "There was an error creating account")
        #     return render(request, 'acct/register.html')
    else:
        return render(request, 'acct/register.html')
