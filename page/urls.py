from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('category', views.category, name='category'),
    path('single', views.single, name='single'),
    path('contact', views.contact, name='contact'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),    
]