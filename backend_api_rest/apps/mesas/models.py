from django.db import models
from apps.users.models import User

# Create your models here.
class Mesa(models.Model):
  id = models.AutoField(primary_key=True,  editable=False)
  user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='Usuario ID')
  number_name = models.CharField('Numero', max_length = 3)
  capacity = models.PositiveIntegerField('Capacidad')
  available = models.BooleanField('Disponibilidad', default = True)

  class Meta:
    verbose_name = 'Mesa'
    verbose_name_plural = 'Mesas'

  def __str__(self):
    return {self.number_name}