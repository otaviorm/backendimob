from django.shortcuts import render, redirect
from .models import Pessoa, Anuncio
from django.http import HttpResponse
from django.core.serializers import serialize
import json


def recuperar_anuncios(request):
    pessoas = Anuncio.objects.all()
    pessoas = serialize('json', pessoas)
    return HttpResponse(pessoas, content_type="application/json")



def salvar(request):
    titulo= request.POST.get("titulo")
    qtd_quartos = request.POST.get("qtd_quartos")
    qtd_banheiro = request.POST.get("qtd_banheiro")
    valor = request.POST.get("valor")
    Anuncio.objects.create(titulo=titulo, qtd_quartos=qtd_quartos, qtd_banheiro=qtd_banheiro, valor=valor)
    return HttpResponse({}, content_type="application/json")


def editar_anuncio(request, id):
    body = json.loads(request.body)
    titulo= body["titulo"]
    qtd_quartos = body["qtd_quartos"]
    qtd_banheiro = body["qtd_banheiro"]
    valor = body["valor"]
    
    anuncio = Anuncio.objects.get(id=id)
    anuncio.titulo = titulo
    anuncio.qtd_quartos = qtd_quartos
    anuncio.qtd_banheiro = qtd_banheiro
    anuncio.valor = valor
    anuncio.save()
    
    return HttpResponse({}, content_type="application/json")


def deletar_anuncio(request, id):
    anuncio = Anuncio.objects.get(id=id)
    anuncio.delete()
    return HttpResponse({}, content_type="application/json")