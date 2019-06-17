from django.shortcuts import render
from .models import Produto

def home(request):
    nome = 'Django jango'
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})
