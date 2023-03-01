from django.db import models


class Linea(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    distancia = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"


class Estaciones(models.Model):
    nombre_estacion = models.CharField(max_length=100)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_estacion}"


class Incidencia (models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField()
    estacion = models.ForeignKey(Estaciones, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return f"{self.estacion} ({self.estacion.linea})"
# Create your models here.
