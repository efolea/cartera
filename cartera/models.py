from django.db import models
from django.utils import timezone
# Create your models here.
class entradas(models.Model):
    #ID=models.AutoField()
    f_apertura=models.DateTimeField()
    f_cierre=models.DateTimeField()
    f_modificado=models.DateTimeField()
    estado=models.CharField(max_length=200)
    ticket=models.CharField(max_length=200)
    tipo=models.CharField(max_length=200)
    divisa=models.DecimalField(max_digits=6, decimal_places=5)
    stop=models.DecimalField(max_digits=11, decimal_places=5)
    n_acciones=models.IntegerField()
    comision_c=models.DecimalField(max_digits=5, decimal_places=2)
    comision_v=models.DecimalField(max_digits=5, decimal_places=2)
    p_compra=models.DecimalField(max_digits=8, decimal_places=5)
    p_venta=models.DecimalField(max_digits=8, decimal_places=5)
    p_actual=models.DecimalField(max_digits=8, decimal_places=5)
    def guradar(self):
        self.f_modificado=timezone.now()
        self.save()
    def __str__(self):
        return self
