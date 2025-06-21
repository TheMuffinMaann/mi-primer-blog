from django.urls import path
from . import views

urlpatterns = [
    path('evaluacion2/', views.lista_public, name='lista_public'),
]