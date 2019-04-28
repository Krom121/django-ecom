from django.shortcuts import render, reverse
from .forms import SnippetForm
from django.http import HttpResponseRedirect
from django.contrib import messages



def index(request):
    return render(request, "index.html", {'title': 'Home'})


def about(request):
    return render(request, 'about.html', {'title': 'About'})


def contact(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you We will be in contact soon')
        return HttpResponseRedirect(reverse('home'))    
    form = SnippetForm()
    return render(request, "contact.html", {'form':form}, {'title': 'Contact'})

def product_list(request):
    return render(request, 'list.html', {'title': 'Shop'})

def post_list(request):
    return render(request, 'blog_list.html', {'title': 'blog'})

def register(request):
    return render(request, 'users/register.html', {'title': 'register'})