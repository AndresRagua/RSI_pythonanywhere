from django.db import models
from django.db.models import Model

# Create your models here.

class Programa(models.Model):
    nombre = models.CharField(max_length=100, null= True, blank= True)
    conductor = models.CharField(max_length=50, null= True, blank= True)
    certificadoLoc = models.CharField(max_length=50, null= True, blank= True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Programacion(models.Model):
    nombre = models.CharField(max_length=100, null= True, blank= True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    fecha = models.DateField(verbose_name='Fecha de Transmision',null = True, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    programa = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-fecha', 'nombre']

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=60)
    numero = models.CharField(max_length=30)
    mensaje = models.TextField()

class Publicidad(models.Model):
    nombre = models.CharField(max_length=50)
    informacion = models.CharField(max_length=1000)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    informacion = models.CharField(max_length=1000)
    link = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

class UsuariosHilo(models.Model):
    nombre = models.CharField(max_length=150, null=True, blank= True)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    url = models.CharField(max_length=210)
    email = models.CharField(max_length=210, null=True, blank=True)

class Cania(models.Model):
    nombre = models.CharField(max_length=100, null= True, blank= True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)

    class Meta:
        ordering = ['id', 'nombre']