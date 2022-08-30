from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente, Producto
from .forms import AddClienteForm, EditarClienteForm

# Create your views here.

def ventas_view(request):
    num_ventas = 156
    context = {
        'num_ventas' : num_ventas
    }
    return render(request, 'ventas.html', context)

def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()
    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar
    }
    return render(request, 'clientes.html', context)

def add_cliente_view(request):
    if request.POST:
        form  = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, 'Error al guardar Cliente.')
                return redirect('Clientes')
    return redirect('Clientes')

def edit_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(request.POST, request.FILES, instance= cliente)
        if form.is_valid:
            form.save()

    return redirect('Clientes')

def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()

    return redirect('Clientes')