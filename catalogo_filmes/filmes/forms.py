from django import forms
from .models import Filme


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'ano', 'diretor', 'genero', 'sinopse', 'poster', 'nota_imdb', 'categorias']