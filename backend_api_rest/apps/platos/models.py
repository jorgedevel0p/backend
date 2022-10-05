from django.db import models

# Create your models here.
class Plato(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField('Nombre Plato', max_length=150)
    description = models.CharField('Descripción', max_length=150)
    recipe = models.TextField('Receta')
    value = models.PositiveIntegerField('Valor Plato')
    type_dish = models.CharField('Tipo de Plato', max_length=150) 

    class Meta:
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'

    def __str__(self):
        return {self.name}
