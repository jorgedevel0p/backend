from django.db import models
from apps.mesas.models import Mesa

# Create your models here.
class Orden(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    mesa = models.ForeignKey("mesas.Mesa", on_delete=models.CASCADE, verbose_name='Mesa ID')
    date = models.DateField('Fecha')
    start_time = models.DateTimeField('Hora Inicio')
    end_time = models.DateTimeField('Hora Termino')
    number_people = models.PositiveIntegerField('Número de Personas')
    state = models.BooleanField('Disponibilidad', default=True)
    

    class Meta:
        verbose_name='Orden'
        verbose_name_plural='Ordenes'
    
    def __str__(self):
        return f'{self.id} {self.state}'