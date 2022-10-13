from django.db import models
from apps.proveedores.models import Proveedor 
from apps.pedidos_proveedor.models import PedidoProveedor

# Create your models here.
class Factura(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    pedido_proveedor = models.OneToOneField("pedidos_proveedor.PedidoProveedor", on_delete=models.CASCADE, verbose_name=' Pedido Proveedor ID')
    proveedor = models.ForeignKey("proveedores.Proveedor", on_delete=models.CASCADE, verbose_name='Proveedor ID')
    date = models.DateField('Fecha Facturación')

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return {self.Factura}