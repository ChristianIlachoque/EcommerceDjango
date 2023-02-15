from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.index, name="index"),
    path('things/', views.things, name="things"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
]