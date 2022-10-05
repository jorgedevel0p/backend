from django.db import models
from apps.ordenes.models import Orden 
from apps.platos.models import Plato 
from apps.productos.models import Producto 

# Create your models here.
class DetalleOrden(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    orden_id = models.ForeignKey("ordenes.Orden", on_delete=models.CASCADE, verbose_name='Orden ID')
    plato_id = models.ForeignKey("platos.Plato", on_delete=models.CASCADE, verbose_name='Plato ID')
    producto_id = models.ForeignKey("productos.Producto", on_delete=models.CASCADE, verbose_name='Producto ID')
    number_dish = models.PositiveIntegerField('Cantidad de Platos') 

    class Meta:
        verbose_name='Detalle Orden'
        verbose_name_plural='Detalle Ordenes'

    def __str__(self):
        return f'Detalle Orden ID: {self.id}'