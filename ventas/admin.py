from django.contrib import admin
# from .models import Cliente, Producto, Venta, DetVenta
from .models import Cliente, Producto, Empresa

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','telefono','codigo')
    search_fields = ['nombre']
    readonly_fields = ('created','updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cliente, ClienteAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','cantidad','costo')
    search_fields = ['descripcion']
    readonly_fields = ('created','updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)

'''
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente_id','subtotal', 'iva', 'total','created')
    search_fields = ['cliente_id']
    readonly_fields = ['created']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Venta, VentaAdmin)

----------------------------------

class DetVentaAdmin(admin.ModelAdmin):
    list_display = ('venta','producto_id', 'precio', 'cantidad', 'subtotal')
    search_fields = ['venta']
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(DetVenta, DetVentaAdmin)


class DetVentaInline(admin.TabularInline):
    model = DetVenta

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente_id', 'subtotal', 'iva', 'total', 'created')
    inlines = (DetVentaInline,)

admin.site.register(Venta, VentaAdmin)
'''

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre','domicilio','telefono')
    search_fields = []
    readonly_fields = ('created','updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Empresa,EmpresaAdmin)


