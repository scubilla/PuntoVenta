__author__ = 'Usuario'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ventas_view, name='Ventas'),
    path('clientes/', views.clientes_view, name='Clientes'),
    path('add_clientes/', views.add_cliente_view, name='AddCliente'),
    path('edit_clientes/', views.edit_cliente_view, name='EditCliente'),
    path('delete_clientes/', views.delete_cliente_view, name='DeleteCliente'),
    path('productos/', views.productos_view, name='Productos'),
    path('add_producto/', views.add_producto_view, name='AddProducto'),
    path('edit_productos/', views.edit_producto_view, name='EditProducto'),
    path('delete_productos/', views.delete_producto_view, name='DeleteProducto'),
    path('add_venta/',views.add_ventas.as_view(), name='AddVenta'),
    path('export/', views.export_pdf_view, name="ExportPDF"),
    path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF"),
]

