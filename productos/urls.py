from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaProductosView, name='listaProdcutosView'),
    path('<int:id>/', views.verProdcutoView, name='verProductoView'),
    path('create/', views.crearProductoView, name='crearProductoView'),
    path('delete/<int:id>/', views.eliminarProductoView, name='eliminarProductoView'),
    path('editar/<int:id>/', views.editarProductoView, name='editarProductoView')
]