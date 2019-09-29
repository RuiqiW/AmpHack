from django.urls import include, path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]