
from django.urls import path
from .views import (
    burger,
    pizza, 
    index,
    order,
    )


app_name = 'food'
urlpatterns = [
    path('index', index, name="index" ),
    path('burger', burger, name="burger" ),
    path('pizza', pizza, name="pizza"),
    path('order', order, name="order" ),


]

