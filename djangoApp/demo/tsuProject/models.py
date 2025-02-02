from django.db import models

# Create your models here.
class Curso(models.Model):
    idCurso = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=60)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.creditos)
