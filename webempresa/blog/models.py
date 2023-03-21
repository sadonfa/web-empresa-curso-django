from pyexpat import model
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Modificacion')

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created_ad']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(default=now, verbose_name='Publicado')
    image = models.ImageField(upload_to='blog', verbose_name='Imagen', null=True, blank=True)
    autorh = models.ForeignKey(User, verbose_name='Autor',on_delete=models.CASCADE )
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name="get_posts")
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Modificacion')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_ad']

    def __str__(self):
        return self.title

    