from django.db import models
from apps.proveedores.models import Proveedor

# Create your models here.
class PedidoProveedor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    proveedor = models.ForeignKey("proveedores.Proveedor", on_delete=models.CASCADE)
    date = models.DateTimeField('Fecha')
    total_value = models.PositiveIntegerField('Valor Total')
    state = models.CharField('Estado de Pago', max_length=150)

    class Meta:
        verbose_name = 'Pedido Proveedor'
        verbose_name_plural = 'Pedidos Proveedor'

    def __str__(self):
        return {self.PedidoProveedor}

