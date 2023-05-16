from django.urls import path
from . import views

# aqui vienen las urls para que se conecte

urlpatterns = [
    
    path ('', views.inicio, name= 'inicio'),
    path ('acerca', views.acerca, name='acerca'),
    path ('taxis', views.taxis, name='taxis'),
    path ('index', views.indexTaxis, name='indexTaxis'),
   
    
]