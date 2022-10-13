from django.db import models

# Create your models here.
class Caja(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    daily_total_value = models.IntegerField('Valor Total diario')

    class Meta:
        verbose_name='Caja'
        verbose_name_plural='Cajas'

    def __str__(self):
        return f' Caja {self.id}'