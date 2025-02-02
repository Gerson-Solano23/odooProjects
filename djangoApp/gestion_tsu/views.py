from django.shortcuts import render
from .models import Proyecto

def lista_proyectos(request):
    proyectos = Proyecto.objects.all()  # Obtener todos los proyectos
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})