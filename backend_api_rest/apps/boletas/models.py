from django.db import models
from apps.ordenes.models import Orden
from apps.users.models import User

# Create your models here.
class Boleta(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='Usuario ID')
    orden = models.ForeignKey('ordenes.Orden', related_name="boletas", on_delete=models.CASCADE, verbose_name='Orden ID')
    value = models.PositiveIntegerField('Valor')
    tip = models.PositiveIntegerField('Propina')
    payment_method = models.CharField('Método de Pago', max_length=150)
    date = models.DateField('Fecha')
    time = models.TimeField('Hora')
    state = models.CharField('Estado de Pago', max_length=150)

    class Meta:
        verbose_name='Boleta'
        verbose_name_plural='Boletas'

    def __str__(self):
        return {self.Boleta}