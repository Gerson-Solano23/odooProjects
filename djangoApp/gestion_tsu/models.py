from django.db import models

class Proyecto(models.Model):
    ESTADOS = [('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado')]
    titulo = models.CharField(max_length=100)
    estudiante = models.CharField(max_length=50)  # Nombre simple para practicar
    documento = models.FileField(upload_to='documentos/')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo