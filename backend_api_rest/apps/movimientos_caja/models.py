from django.db import models
from apps.boletas.models import Boleta
from apps.facturas.models import Factura

# Create your models here.
class MovimientoCaja(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    boleta = models.ForeignKey("boletas.Boleta", on_delete=models.CASCADE, verbose_name='Boleta ID')
    factura = models.ForeignKey("facturas.Factura", on_delete=models.CASCADE, verbose_name='Factura ID')
    date_mov = models.DateTimeField('Fecha Movimiento')
    initial_balance = models.IntegerField('Saldo Inicial')

    class Meta:
        verbose_name = 'Movimiento Caja'
        verbose_name_plural = 'Movimientos Caja'

    def __str__(self):
        return {self.MovimientoCaja}