from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # go to views.py in function index
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
]
