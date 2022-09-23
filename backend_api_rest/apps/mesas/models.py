from django.db import models

# Create your models here.
class Mesa(models.Model):
  id = models.AutoField(primary_key=True,  editable=False)
  number_name = models.CharField('Numero', max_length = 3)
  available = models.BooleanField(default = True)
  capacity = models.PositiveIntegerField()

  class Meta:
    verbose_name = 'Mesa'
    verbose_name_plural = 'Mesas'

  def __str__(self):
    return {self.number_name}