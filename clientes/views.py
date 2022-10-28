from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def clientes_view(request):
    return render(request, 'clientes.html')



