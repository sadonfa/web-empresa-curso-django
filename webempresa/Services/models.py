from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Service(models.Model):
       
    title = models.CharField(max_length=150, verbose_name='Titulo' )
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services', verbose_name='Imagen')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Modificado')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = "Servicios"
        ordering = ['-title']
    
    def __str__(self):
        return self.title