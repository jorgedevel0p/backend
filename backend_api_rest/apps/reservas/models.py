from django.db import models
from apps.users.models import User
from apps.mesas.models import Mesa
# Create your models here.

class Reserva(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name="Usuario ID")
    mesa = models.ForeignKey("mesas.Mesa", on_delete=models.CASCADE, verbose_name="Mesa ID")
    status = models.CharField('Estado', max_length=100)

    class Meta:
        verbose_name= 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return {self.id}
