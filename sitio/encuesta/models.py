from django.db import models

from django.utils import timezone
import datetime
# Create your models here.
class Pregunta (models.Model):
    texto_pregunta = models.CharField(max_length=500)
    fecha = models.DateTimeField('fecha de publicacion')
    def __str__(self):
        return self.texto_pregunta



class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto_respuesta = models.CharField(max_length=500)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.texto_respuesta

    def publicado_recientemente(self):
        return self.fecha >= timezone.now() - datetime(days=1)