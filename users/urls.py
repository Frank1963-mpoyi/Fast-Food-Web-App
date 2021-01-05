
from django.urls import path
from .views import signup, login_n, logout_n


app_name= 'users'
urlpatterns = [
    path('signup', signup, name="signup"),
    path('login', login_n, name="login"),
    path('logout', logout_n, name="logout"),
]

