from django.db import models

# Create your models here.
class PreciosTabla(models.Model):
    corte = models.CharField(verbose_name="Corte", max_length=100)
    precio = models.CharField(verbose_name="Precio", max_length=100)

    class Meta:
        verbose_name = "corte"
        verbose_name_plural = "cortes"
        ordering = ['corte']

    def __str__(self) -> str:
        return self.corte

class Ofertas(models.Model):
    oferta = models.CharField(verbose_name="Oferta", max_length=100)
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)

    class Meta:
        verbose_name = "oferta"
        verbose_name_plural = "ofertas"
        ordering = ['oferta']

    def __str__(self) -> str:
        return self.oferta
    