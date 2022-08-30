__author__ = 'Usuario'
# crear formualarios basados en modelos para personalizarlos
from django import forms
from ventas.models import Cliente

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre','telefono')  # tupla para mostrar
        labels = {
            'codigo': 'Codigo Cliente',
            'nombre': 'Nombre Cliente',
            'telefono': 'Telefono (Contacto)',
        }

class EditarClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo','nombre','telefono')  # tupla para mostrar
        labels = {
            'codigo': 'Codigo Cliente:',
            'nombre': 'Nombre Cliente:',
            'telefono': 'Telefono (Contacto):',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type':'text', 'id':'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id':'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id':'telefono_editar'}),
        }
