from django.db import models

# Create your models here.
class Mesa(models.Model):
  id = models.UUIDField(primary_key=True,  editable=False)
  number_name = models.CharField('Numero', max_length = 3)
  available = models.BooleanField(default = True)
  capacity = models.PositiveIntegerField()