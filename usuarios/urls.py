from django.urls import path
from . import views

urlpatterns = [
    path("", views.listaUsuariosView, name="listaUsuariosView"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("<int:id>/", views.verUsuarioView, name="verUsuarioView"),
    path("create/", views.crearUsuarioView, name="crearUsuarioView"),
    path("delete/<int:id>/", views.eliminarUsuarioView, name="eliminarUsuarioView"),
    path("edit/<int:id>/", views.editarUsuarioView, name="editarUsuarioView"),
]