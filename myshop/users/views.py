from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

"""
Below is the user register form created with the user creation form
I am using flash messages to let the user know whts happened on completion
of the form.
User is then redirected to the login page.

"""
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

"""

below I am using the login required decorator to only a user who is 
login to view the profile page.

"""
@login_required
def profile(request):
    return render(request, 'users/profile.html', {})