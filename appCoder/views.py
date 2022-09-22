import re
from django.shortcuts import render
from django.http import HttpResponse
from appCoder.models import Estudiante
# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def home(request):
    return render(request, "home.html")


def cursos(request):
    return render(request, "cursos.html")

def profesores(request):
    return render(request, "profesores.html")
   
def estudiantes(request):
    if request.method == "POST": 
        estudiante = Estudiante(nombre= request.POST ['nombre'], apellido= request.POST ['apellido'], email = request.POST['email'])
        estudiante.save()
        return render(request, "home.html")
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")

