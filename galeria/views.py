from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import fotografia
from django.contrib import messages




# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "usuário não logado")
        return redirect('login')

    fotografias = fotografia.objects.order_by("data_publicada").filter(publicada = True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    Fotografia = get_object_or_404(fotografia, pk = foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": Fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "usuário não logado")
        return redirect('login')
    fotografias = fotografia.objects.order_by("data_publicada").filter(publicada = True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)


    return render(request, "galeria/buscar.html", {"cards": fotografias})