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
    vagas = request.POST.get("vagas")
    descricao = request.POST.get("descricao")
    tamanho = request.POST.get("tamanho")
    endereco = request.POST.get("endereco")
    url_imagem = request.POST.get("url_imagem")
    Anuncio.objects.create(titulo=titulo,
                            qtd_quartos=qtd_quartos,
                            qtd_banheiro=qtd_banheiro,
                            valor=valor, vagas=vagas,
                            descricao=descricao,
                            tamanho=tamanho,
                            endereco=endereco,
                            url_imagem=url_imagem)
    
    return HttpResponse({}, content_type="application/json")


def editar_anuncio(request, id):
    body = json.loads(request.body)
    titulo= body["titulo"]
    qtd_quartos = body["qtd_quartos"]
    qtd_banheiro = body["qtd_banheiro"]
    valor = body["valor"]
    vagas = body["vagas"]
    descricao = body["descricao"]
    tamanho = body["tamanho"]
    endereco = body["endereco"]
    url_imagem = body["url_imagem"]
    
    anuncio = Anuncio.objects.get(id=id)
    anuncio.titulo = titulo
    anuncio.qtd_quartos = qtd_quartos
    anuncio.qtd_banheiro = qtd_banheiro
    anuncio.valor = valor
    anuncio.vagas = vagas
    anuncio.descricao = descricao
    anuncio.tamanho = tamanho
    anuncio.endereco = endereco
    anuncio.url_imagem = url_imagem
    anuncio.save()
    
    return HttpResponse({}, content_type="application/json")


def deletar_anuncio(request, id):
    anuncio = Anuncio.objects.get(id=id)
    anuncio.delete()
    return HttpResponse({}, content_type="application/json")