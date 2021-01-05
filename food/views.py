from django.shortcuts import render
from .models import Pizza, Burger
#from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required



#@staff_member_required

def index (request):
    template_name ='food/index.html'
    
    context={'active_link':'index'}
    return render (request, template_name, context)


@login_required(login_url='users:login')
def burger (request):
    template_name ='food/burger.html'
    queryset = Burger.objects.all()
    context={
        'queryset': queryset,
        'active_link':'burger'
        }
    return render (request, template_name, context)


@login_required(login_url='users:login')
def pizza (request):
    template_name = 'food/pizza.html'
    queryset= Pizza.objects.all()
    context= {
        'queryset': queryset,
        'active_link':'pizza'
        }
    return render (request, template_name, context)


@login_required(login_url='users:login')
def order (request):
    template_name ='food/orders.html'
    
    context={'active_link':'orders'}
    return render (request, template_name, context)
