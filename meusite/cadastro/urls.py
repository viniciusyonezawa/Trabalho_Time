from django.urls import path
from . import views
urlpatterns = [
    path('',views.ola_mundo, name='time'),
    path('',views.segundapagina, name='segundapagina'),
]