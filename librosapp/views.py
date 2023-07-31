from django.shortcuts import render, redirect
from .forms import LibroForm, ClienteForm, CompraForm
from .forms import BusquedaLibrosForm
from .models import Libro

# Create your views here.
def index(request):
    return render(request, "librosapp/index.html")


def agregar_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_libro")
    else:
        form = LibroForm()
    return render(request, "librosapp/agregar_libro.html", {"form": form})


def agregar_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_cliente")
    else:
        form = ClienteForm()
    return render(request, "librosapp/agregar_cliente.html", {"form": form})


def agregar_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agregar_compra")
    else:
        form = CompraForm()
    return render(request, "librosapp/agregar_compra.html", {"form": form})


def buscar_libros(request):
    if request.method == "GET":
        form = BusquedaLibrosForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            autor = form.cleaned_data["autor"]

            libros = Libro.objects.filter(
                titulo__icontains=titulo, autor__icontains=autor
            )

            return render(
                request,
                "librosapp/resultados_busqueda.html",
                {"libros": libros, "form": form},
            )

    # Si no se envió el formulario o no es válido, mostramos el formulario vacío
    else:
        form = BusquedaLibrosForm()

    return render(request, "librosapp/busqueda_libros.html", {"form": form})
