from django.urls import path
from . import views

from ProyectoWebApp import views

urlpatterns = [

    path('',views.home, name="home"),
    path('crear_pasajero/', views.crear_pasajero, name='crear_pasajero'),
    path('contacto/',views.contacto, name='contacto'), 
    path('servicios', views.servicios, name="servicios"),
    path('enviar_contacto/', views.enviar_contacto, name='enviar_contacto'),  
    path('crear-vuelo/', views.crear_vuelo, name='crear_vuelo'),
    path('crear-pasaje/', views.crear_pasaje, name='crear_pasaje'),
    

]
