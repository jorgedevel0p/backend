from django.db import models

# Create your models here.
class Plato(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    recipe = models.TextField()
    value = models.PositiveIntegerField()
    type_dish = models.CharField(max_length=150) 

    class Meta:
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'

    def __str__(self):
        return {self.name}
