from django.urls import path
from . import views,login


urlpatterns = [
    path('', views.HomePage, name='home'),
    path('login' ,login.LoginPage, name='login'),
    path('signup', login.SignUp,name='signup')
]

