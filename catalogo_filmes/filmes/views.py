# Sistema simples de catálogo de filmes com CRUD e integração com API externa (OMDb)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Filme
from .forms import FilmeForm
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Exibe todos os filmes cadastrados
def lista_filmes(request):
    filmes = Filme.objects.all().order_by('-id')
    return render(request, 'filmes/lista_filmes.html', {'filmes': filmes})


# Criação de um novo filme
def criar_filme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()

    return render(request, 'filmes/form_filme.html', {'form': form})


# Edição de um filme existente
def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm(instance=filme)

    return render(request, 'filmes/form_filme.html', {'form': form})


# Exclusão de um filme
def excluir_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)

    if request.method == 'POST':
        filme.delete()
        return redirect('lista_filmes')

    return render(request, 'filmes/excluir_filme.html', {'filme': filme})


# Busca de filme usando API externa
def buscar_filme_api(request):
    filme = None
    erro = None

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        api_key = os.getenv('OMDB_API_KEY')

        url = "https://www.omdbapi.com/"
        params = {
            't': titulo,
            'apikey': api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        if data.get('Response') == 'True':
            filme = data
        else:
            erro = data.get('Error', 'Filme não encontrado.')

    return render(request, 'filmes/buscar_filme.html', {
        'filme': filme,
        'erro': erro
    })


# Create your views here.
