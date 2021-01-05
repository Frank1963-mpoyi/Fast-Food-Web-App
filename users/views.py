from django.shortcuts import render, redirect
from .forms import NewUserForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def signup(request):
    template_name = "users/sign-up.html"

    form = NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:pizza')
    context = dict( form =NewUserForm())
    return render(request, template_name, context)


def login_n(request): # i change login 
    template_name ='users/login.html'
    
    if request.POST:
        username = request.POST.get('username')
        pwd      = request.POST.get('password')
        
        user = authenticate(request, username=username, password=pwd)
        if user is not None: # which means is authenticate
            login(request, user)# this login is a django function
            return redirect('food:pizza')
    else:
        messages.info(request, 'username and/or password are incorrect')
        #messages.info(request, 'Three credits remain in your account.')
    context ={'active_link': 'login'}
    return render (request, template_name, context)
    