from django import forms
from .models import Libro, Cliente, Compra


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ("titulo", "autor", "precio")


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ("nombre", "email")


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ("cliente", "libro", "fecha_compra")


class BusquedaLibrosForm(forms.Form):
    titulo = forms.CharField(required=False)
    autor = forms.CharField(required=False)
