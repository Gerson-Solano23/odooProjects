from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello),
    path('cursos', views.home),
    path('cursos/registrarCurso/', views.registrarCurso),
path('cursos/edicionCurso/<idCurso>', views.edicionCurso),
path('cursos/editarCurso/', views.editarCurso, name='editarCurso'),
path('cursos/eliminarCurso/<idCurso>', views.eliminarCurso),

]