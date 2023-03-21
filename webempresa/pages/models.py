from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    
    title = models.CharField( 
        verbose_name="Titulo", max_length=200)
    content = RichTextField(
        verbose_name="Contenido")
    created_ad = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True)
    updated_ad = models.DateTimeField(
        verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ['title']

    def __str__(self):
        return self.title