from django.db import models

# Create your models here.
class Product(models.Model):
    id = autoField(primary_key = True)
    state = models.BooleanField('Estado',   default=True)
    name = models.CharField('Nombre', max_length=150)
    # stock = models.PositiveIntegerField('Stock')
    # expiration_date = modes.DateField('Fecha de Vencimiento')
    # measure_unit = models.CharField('Unidad de Medida', max_length=50, blank=False, null=False, unique=True)
    # category_product = models.CharField('Categoría de Producto', max_length=50, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return {self.name}