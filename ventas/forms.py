__author__ = 'Usuario'
# crear formualarios basados en modelos para personalizarlos
from django import forms
from .models import Cliente, Producto

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


# *******************************************
# PRODUCTOS
# *******************************************

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion','imagen', 'costo', 'precio', 'cantidad')  # tupla para mostrar
        labels = {
            'codigo': 'Cod. Barras:',
            'descripcion': 'Descripcion del producto:',
            'imagen': 'Imagen:',
            'costo': 'Costo Gs:',
            'precio': 'Precio Gs:',
            'cantidad': 'Cantidad:',

        }

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo','descripcion','imagen','costo','precio','cantidad' )  # tupla para mostrar
        labels = {
            'codigo': 'Codigo/Barras:',
            'descripcion': 'Nombre:',
            'imagen': 'Imagen:',
            'costo': 'Costo Gs.:',
            'precio': 'Precio Gs.:',
            'cantidad': 'Existencia:',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'id':'codigo_editar'}),
            'descripcion': forms.TextInput(attrs={'id':'descripcion_editar'}),
            'costo': forms.TextInput(attrs={'id':'costo_editar'}),
            'precio': forms.TextInput(attrs={'id':'precio_editar'}),
            'cantidad': forms.TextInput(attrs={'id':'cantidad_editar'}),

        }


#****************
# FORMS DE VENTA
#****************
'''
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder': 'Ingrese descripción',
                    'row': 3,
                    'cols': 5
                }
            ),
        }
'''