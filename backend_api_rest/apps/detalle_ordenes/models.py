from django.db import models
from apps.ordenes.models import Orden 
from apps.platos.models import Plato 
from apps.productos.models import Producto 

# Create your models here.
class DetalleOrden(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    orden = models.ForeignKey("ordenes.Orden", related_name="detalle_ordenes", on_delete=models.CASCADE, verbose_name='Orden ID')
    plato = models.ForeignKey("platos.Plato", related_name="detalle_ordenes_plato", on_delete=models.CASCADE, verbose_name='Plato ID')
    producto = models.ForeignKey("productos.Producto", related_name="detalle_ordenes_producto", on_delete=models.CASCADE, verbose_name='Producto ID')
    number_dish = models.PositiveIntegerField('Cantidad de Platos') 

    class Meta:
        verbose_name='Detalle Orden'
        verbose_name_plural='Detalle Ordenes'

    def __str__(self):
        return f'Detalle Orden ID: {self.DetalleOrden}'