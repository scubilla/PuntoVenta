from django.db import models
from django.forms import model_to_dict  # transformar a tipo JSON un modelo

# Create your models here.

class Cliente(models.Model):
    codigo = models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=False)
    telefono = models.CharField(max_length=200, null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    codigo = models.CharField(max_length=255, unique=True, null=True, blank=True)
    descripcion = models.CharField(max_length=255, unique=True, null=False)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    precio = models.DecimalField(max_digits=15, decimal_places=2, null=False, default=0, blank=True )
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        order_with_respect_to = 'descripcion'

    def __str__(self):
        return self.descripcion

'''
class Venta(models.Model):
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=10.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente_id.nombre

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class DetVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.producto_id.descripcion

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
        
       
    class detalle_factura(models.Model):
    factura = models.ForeignKey(factura, db_column='factura_id')
    cliente = models.IntegerField(null=True, blank=True)
    producto = models.ForeignKey(producto, db_column='producto_id')
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    def  __unicode__(self):
    return self.subtotal
   
        

class DetVenta(models.Model):
    venta = models.ForeignKey(Venta, db_column='venta_id', on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, db_column='producto_id', on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = (self.precio*self.cantidad)
        super(DetVenta, self).save(*args, **kwargs)

    def __str__(self):
        return self.producto_id.descripcion

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']
'''


class Egreso(models.Model):
    fecha_pedido = models.DateField(max_length=255)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name='clientee')
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    pagado = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    comentarios = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    ticket = models.BooleanField(default=True)
    desglosar = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'egreso'
        verbose_name_plural = 'egresos'
        order_with_respect_to = 'fecha_pedido'

    def __str__(self):
        return str(self.id)


class ProductosEgreso(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2, null=False)
    precio = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    iva = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    created = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=True)
    devolucion = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'producto egreso'
        verbose_name_plural = 'productos egreso'
        order_with_respect_to = 'created'

    def __str__(self):
        return self.producto

    def toJSON(self):
        item = model_to_dict(self, exclude=['created'])
        return item
