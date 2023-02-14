from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaVentasDetallesView, name='listaVentasDetallesView'),
    path('<int:id>/', views.verVentaDetallesView, name='verVentaDetallesView'),
    path('create/', views.crearVentaDetallesView, name='crearVentaDetallesView'),
    path('delete/<int:id>/', views.eliminarVentaDetallesView, name='eliminarVentaDetallesView'),
    path('edit/<int:id>/', views.editarVentaDetallesView, name='editarVentaDetallesView')
]