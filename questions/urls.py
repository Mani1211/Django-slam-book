from django.urls import path 
from . import views

urlpatterns = [
    path('questions',views.questions,name="questions"),
    path('',views.home,name="home"),
    path('thank',views.thank,name='thank')
]
