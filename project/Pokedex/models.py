from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    numero = models.IntegerField(null=True)
    habilidad = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Entrenador(models.Model):
    nombre = models.CharField(max_length=200)
    ciudad_de_origen = models.CharField(max_length=200)
    edad = models.IntegerField()
    historia = models.TextField()

    def __str__(self):
        return self.nombre
