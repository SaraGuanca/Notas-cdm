from django.db import models

# Create your models here
class Alumno(models.Model):
    nombre = models.CharField(max_length=10,null=True, default=None)
    apellido = models.CharField
    dni = models.CharField(max_length=8, null=True, default=None)
    
    def __str__(self):
        return f"Nombre: {self.nombre} = apellido: {self.apellido} = dni: {self.dni}"
    
class Curso(models.Model):
    alumnos = models.ForeignKey(
        Alumno,
        related_name= 'alumno',
        on_delete= models.CASCADE,
        verbose_name= 'alumno',
        null=True,
        default=None
    ) 
    año = models.DateTimeField(null=False)
    division= models.CharField(max_length=1, null=False )
    año_calendario= models.DateTimeField(null=False)
class Notas(models.model): 
    alumnos = models.ForeignKey(
        Alumno,
        related_name= 'alumno_curso'
        on_delete= models.CASCADE,
        verbose_name='alumno_curso'
        null=True,
        default=None
    )
    valor= models.FloatField()
    descripcion= models.Charfield(max_length=256, blank=True)
    nombre_materia= models.CharField(max_length=10, null=False)

class Materia(models.model):
    alumnos= models.ForeignKey(
        Alumno
        related_name= 'alumno_materia'
        on_delete= models.CASCADE
        verbose_name= 'alumno_materia'
        null=True,
        default=None
    )
    nombre_materia= models.CharField(max_length=10, null = False)

