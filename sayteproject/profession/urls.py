from auth.views import login
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('prosto/', prosto, name='prosto'),
    path('addpage/', addpage,name='addpage'),
    path('conact/', conact, name='conact'),


]