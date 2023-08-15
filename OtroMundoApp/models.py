from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    edad = models.IntegerField()
    hobby = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Clientes"