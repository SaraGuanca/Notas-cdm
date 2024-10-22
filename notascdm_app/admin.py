from django.contrib import admin
from .models import Alumno, Curso, Descripcion, Materia, Nota

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = 'id','apellido','nombre','dni','activo'
    list_filter = 'activo',
    search_fields = 'apellido','nombre','dni'

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = 'id','nombre',
    search_fields = 'nombre',

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = 'id','anio','division','anio_calendario'
    list_filter = 'anio','division',

@admin.register(Nota)
class NotasAdmin(admin.ModelAdmin):
    list_display = 'id','trimestre','materia','alumno','descripcion','descripcion','valor'
    list_filter = 'materia','trimestre','alumno'
    search_fields = 'alumno',
    
class AlumnoInline(admin.TabularInline):
    model = Curso.alumnos.through
    extra = 1  # Define cuántas líneas vacías extra quieres que se muestren.

class CursoAdmin(admin.ModelAdmin):
    inlines = [AlumnoInline]
    exclude = ('alumnos',)  # Para evitar que se muestre el widget default de ManyToMany

@admin.register(Descripcion)
class DescripcionAdmin(admin.ModelAdmin):
    list_display = 'id','descripcion','fecha'
    search_fields = 'descripcion',
    list_filter = 'fecha',