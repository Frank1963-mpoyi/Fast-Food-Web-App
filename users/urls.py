
from django.urls import path
from .views import signup, login


app_name= 'users'
urlpatterns = [
    
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
]
