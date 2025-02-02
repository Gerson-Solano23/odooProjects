from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curso
# Create your views here.
def hello(request):
    return render(request, 'hello.html', {})

def home(request):
    cursos = Curso.objects.all()
    return render(request, 'gestionCursos.html', {"cursos": cursos})

def registrarCurso(request):
    cursos = Curso.objects.all()
    if request.method == 'POST':
        cursoId = request.POST['txtId']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']

        if validarIdCurso(cursoId):
            messages.error(request,  "El id del curso ya existe!")
            return redirect('/tsuProject/cursos')
        else:
            curso=Curso.objects.create(idCurso=cursoId, nombre=nombre, creditos=creditos)
            messages.success(request, "Curso registrado correctamente")
            return redirect('/tsuProject/cursos')
    else:
        return render(request, 'gestionCursos.html', {"cursos": cursos})

def edicionCurso(request, idCurso):
    curso = Curso.objects.get(idCurso=idCurso)
    print(curso.nombre)
    return render(request, 'edicionCurso.html', {"curso": curso})

def editarCurso(request):
    cursoId = request.POST['txtId']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    Curso.objects.filter(idCurso=cursoId).update(nombre=nombre, creditos=creditos)
    messages.success(request, "Curso actualizado correctamente")
    return redirect('/tsuProject/cursos')







def eliminarCurso(request, idCurso):
    curso = Curso.objects.get(idCurso=idCurso)
    curso.delete()
    messages.success(request, "Curso eliminado correctamente")
    return  redirect('/tsuProject/cursos')

def validarIdCurso(cursoId):
    return Curso.objects.filter(idCurso=cursoId).exists()

