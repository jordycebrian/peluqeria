from django.db import models
# Create your models here.

#modelo para agenda cita
class Cita(models.Model):
    servicio = models.CharField(verbose_name="Servicio",max_length=100)
    estilista = models.CharField(verbose_name="Estilista", max_length=100 ,blank=True, null=True)
    dia = models.DateField(verbose_name="Día")
    hora = models.TimeField(verbose_name="Hora")
    correo = models.EmailField(verbose_name="Correo electronico")
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    telefono = models.CharField(verbose_name="Teléfono", max_length=20)
    cantidad = models.CharField(verbose_name="Cantidad", max_length=100, blank=True, null=True)
    descripcion = models.TextField(verbose_name="Descripción", max_length=200,blank=True, null=True)


    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['hora']

    def __str__(self) -> str:
        return self.servicio
