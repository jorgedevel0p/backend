from django.db import models
from apps.productos.models import Producto 

# Create your models here.
class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    producto_id = models.ForeignKey("productos.Producto", on_delete=models.CASCADE, verbose_name='Producto ID' )
    value =  models.PositiveIntegerField('Valor Producto')
    quantity = models.IntegerField('Cantidad Producto')

    class Meta:
        verbose_name = 'Detalle Pedido'
        verbose_name_plural = 'Detalle Pedidos'

        def __str__(self):
            return f'Detalle Pedido ID {self.id}'