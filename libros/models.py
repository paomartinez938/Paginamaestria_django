from django.db import models

# Create your models here.

class Libro(models.Model):
  titulo = models.CharField(max_length=200)
  autor = models.CharField(max_length=100)
  resume = models.TextField()

  def __str__(self):#Representa una instancia de libro como una cadena de texto
    return self.titulo
