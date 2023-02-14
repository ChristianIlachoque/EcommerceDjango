from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaVentasView, name='listaVentasView'),
    path('<int:id>/', views.verVentaView, name='verVentaView'),
    path('create/', views.crearVentaView, name='crearVentaView'),
    path('delete/<int:id>/', views.eliminarVentaView, name='eliminarVentaView'),
    path('edit/<int:id>/', views.editarVentaView, name='editarVentaView')
]