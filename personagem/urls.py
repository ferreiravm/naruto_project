from django.urls import path
from personagem.views import index, imagem

urlpatterns = [
    path('', index),
    path('index.html/', index),
    path('imagem.html/', imagem)
]
