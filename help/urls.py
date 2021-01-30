from django.urls import path
from . import views

urlpatterns = [
    path('', views.help, name='help'),
    path('user', views.our_team, name='team'),
]
