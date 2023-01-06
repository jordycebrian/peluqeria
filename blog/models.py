from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

#categorias del blog
class Category(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de Edición")


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name


#modelo para crear bogs
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateField(auto_now=True, verbose_name="Fehca de Edición")


    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created']


    def __str__(self) -> str:
        return self.title