from django.shortcuts import render, redirect
from .forms import NewUserForm
#from django.contrib.auth.forms import UserCreationForm


def signup(request):
    template_name = "users/sign-up.html"

    form = NewUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:pizza')
    context = dict( form =NewUserForm())
    return render(request, template_name, context)


def login(request):
    template_name ='users/login.html'
    context ={'active_link': 'login'}
    return render (request, template_name, context)
    