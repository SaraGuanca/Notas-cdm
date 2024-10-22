from django.shortcuts import render
from .models import Alumno

# Create your views here.
def index(request):
    return render(request,'notascdm\index.html')

def retornar_alumnos(request):
    alumnos = Alumno.object.all()
    if alumnos:
        context = {
            "listaAlumnos": alumnos
        }
        return render (request, 'notas.html', context)
    return render (request, 'index.html')