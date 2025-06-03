from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Venda, Produto
from .forms import ClienteForm, VendaForm, ProdutoForm
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

# CLIENTE

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})

def criar_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/form.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/form.html', {'form': form})

def remover_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('listar_clientes')

# VENDA

def listar_vendas(request):
    vendas = Venda.objects.all()
    clientes = Cliente.objects.all()

    cliente_id = request.GET.get('cliente')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if cliente_id:
        vendas = vendas.filter(cliente_id=cliente_id)
    if data_inicio:
        vendas = vendas.filter(data_venda__gte=data_inicio)
    if data_fim:
        vendas = vendas.filter(data_venda__lte=data_fim)

    return render(request, 'vendas/listar.html', {
        'vendas': vendas,
        'clientes': clientes
    })

def criar_venda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_vendas')
    return render(request, 'vendas/form.html', {'form': form})

def editar_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    form = VendaForm(request.POST or None, instance=venda)
    if form.is_valid():
        form.save()
        return redirect('listar_vendas')
    return render(request, 'vendas/form.html', {'form': form})

def remover_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    venda.delete()
    return redirect('listar_vendas')

# PRODUTO

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def produto_create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, 'produtos/form.html', {'form': form})

def produto_update(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('produto_list')
    return render(request, 'produtos/form.html', {'form': form})

def produto_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produto_list')