from django.shortcuts import render
from .models import Pizza, Burger



def index (request):
    template_name ='food/index.html'
    
    context={'active_link':'index'}
    return render (request, template_name, context)

def burger (request):
    template_name ='food/burger.html'
    queryset = Burger.objects.all()
    context={
        'queryset': queryset,
        'active_link':'burger'
        }
    return render (request, template_name, context)


def pizza (request):
    template_name = 'food/pizza.html'
    queryset= Pizza.objects.all()
    context= {
        'queryset': queryset,
        'active_link':'pizza'
        }
    return render (request, template_name, context)


def order (request):
    template_name ='food/orders.html'
    
    context={'active_link':'orders'}
    return render (request, template_name, context)
