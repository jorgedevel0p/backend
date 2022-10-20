from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField( max_length=150)
    stock = models.PositiveIntegerField()
    entry_date = models.DateField()
    expiration_date = models.DateField()
    value = models.PositiveIntegerField()
    brand = models.CharField(max_length=150)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return {self.Producto}