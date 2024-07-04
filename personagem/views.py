from django.shortcuts import render


def index(request):
    return render(request, 'personagem/index.html')

def imagem(request):
    return render(request, 'personagem/imagem.html')