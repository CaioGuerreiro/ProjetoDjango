from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name = 'index'),

    path('imagem/<foto_id>', imagem, name = 'imagem'),
    path('buscar', buscar, name = 'buscar')
]