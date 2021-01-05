
from django.urls import path
from .views import signup, login_n


app_name= 'users'
urlpatterns = [
    
    path('login', login_n, name="login"),
    path('signup', signup, name="signup"),
]

