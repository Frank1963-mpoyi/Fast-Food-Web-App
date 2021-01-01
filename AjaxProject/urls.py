
from django.urls import path
from .views import photo_add_view


app_name= 'AjaxProject'
urlpatterns = [

    path('ajax', photo_add_view, name="ajax"),
]

