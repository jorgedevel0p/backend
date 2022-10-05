from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Nombre', max_length=150)
    stock = models.PositiveIntegerField('Stock')
    entry_date = models.DateField('Fecha de Ingreso')
    expiration_date = models.DateField('Fecha de Vencimiento')
    value = models.PositiveIntegerField('Precio')
    brand = models.CharField("Marca", max_length=150)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return {self.name}