from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField('Nombre Proveedor', max_length=150)
    email = models.EmailField('Mail Proveedor', max_length=150)
    phone = models.CharField('Telefono Proveedor', max_length=12)
    state = models.BooleanField('Estado Proveedor', default=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return {self.name}