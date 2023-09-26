from django.shortcuts import render, redirect, get_object_or_404
from .form import ProdutoForm
from .models import Produto

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
        
    else:
        form = ProdutoForm()
    return render(request, 'produtos/novo_produto.html', {'form': form})


def edita_produto(request, codigo):
    produto = get_object_or_404(Produto, codigo=codigo)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/edita_produto.html', {'form': form})

def exclui_produto(request, codigo):
    produto = get_object_or_404(Produto, codigo=codigo)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/exclui_produto.html', {'produto': produto})

