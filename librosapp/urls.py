from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
    path("", index, name="inicio"),
    path("agregar_cliente/", agregar_cliente, name="agregar_cliente"),
    path("agregar_libro/", agregar_libro, name="agregar_libro"),
    path("agregar_compra/", agregar_compra, name="agregar_compra"),
    path("buscar_libros/", views.buscar_libros, name="buscar_libros"),
]
