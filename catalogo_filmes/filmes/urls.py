from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_filmes, name='lista_filmes'),
    path('filmes/novo/', views.criar_filme, name='criar_filme'),
    path('filmes/<int:pk>/editar/', views.editar_filme, name='editar_filme'),
    path('filmes/<int:pk>/excluir/', views.excluir_filme, name='excluir_filme'),
    path('buscar/', views.buscar_filme_api, name='buscar_filme'),
]