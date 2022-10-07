from django.db import models
from apps.productos.models import Producto 
from apps.platos.models import Plato

# Create your models here.
class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    producto_id = models.ForeignKey("productos.Producto", on_delete=models.CASCADE, verbose_name='Producto ID')
    plato_id = models.ForeignKey("platos.Plato", related_name='ingredientes' ,on_delete=models.CASCADE, verbose_name='Plato ID')
    name = models.CharField('Nombre Ingrediente', max_length=150)
    quantity = models.PositiveIntegerField('Cantidad INgrediente')

    class Meta:
        verbose_name='Ingrediente'
        verbose_name_plural='Ingredientes'

    def __str__(self):
        return {self.name}