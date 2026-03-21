from django.db import models

# Modelo de categorias para organizar os filmes
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome


# Modelo principal de filmes
class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    diretor = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=200, blank=True, null=True)
    sinopse = models.TextField(blank=True, null=True)
    poster = models.URLField(blank=True, null=True)
    nota_imdb = models.CharField(max_length=10, blank=True, null=True)

    # Relaciona o filme com várias categorias
    categorias = models.ManyToManyField(Categoria, related_name='filmes', blank=True)

    def __str__(self):
        return self.titulo


# Modelo para listas de filmes
class Lista(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    filmes = models.ManyToManyField(Filme, related_name='listas', blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Create your models here.
