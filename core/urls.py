from django.contrib import admin
from django.urls import path, include
from .views import recuperar_anuncios, salvar, editar_anuncio, deletar_anuncio

urlpatterns = [
    path('', recuperar_anuncios),
    path('salvar/', salvar, name="salvar"),
    path('editar/<int:id>', editar_anuncio, name="editar"),
    path('deletar/<int:id>', deletar_anuncio, name="deletar"),
]