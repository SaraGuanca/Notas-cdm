from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Alumno(models.Model):
    nombre = models.CharField(max_length=30,null=False)
    apellido = models.CharField(max_length=30,null=False)
    dni = models.CharField(max_length=8, null=False)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Materia(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    def __str__(self):
        return self.nombre    


class Curso(models.Model):
    anio = models.IntegerField(null=False,verbose_name='Año')
    division = models.CharField(max_length=1, null=False, verbose_name='División')
    anio_calendario = models.IntegerField(null=False,verbose_name='Año Calendario')
    alumnos = models.ManyToManyField(
        Alumno, 
        related_name='cursos',
        )
    materias = models.ManyToManyField(
        Materia, 
        related_name='cursos',
        )
    def __str__(self) -> str:
        return f"{self.anio}{self.division}"

class Descripcion(models.Model):
    descripcion= models.CharField(max_length=30)
    fecha = models.DateField(null=False, verbose_name="Fecha")
    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name_plural = "Descripciones"
    

class Nota(models.Model): 
    trimestre = models.IntegerField(null=False,verbose_name="Trimestre")
    valor = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    descripcion = models.ForeignKey(
        Descripcion,
        related_name= 'notas',
        on_delete=models.CASCADE,
        verbose_name= "Descripción",
        null=False
    )
    materia = models.ForeignKey(
        Materia,
        related_name= 'notas',
        on_delete=models.CASCADE,
        verbose_name= "Materia",
        null=False
    )
    alumno = models.ForeignKey(
        Alumno,
        related_name= 'notas',
        on_delete= models.CASCADE,
        verbose_name='Alumno',
        null=True
    )
    
    class Meta:
        # Restricción de unicidad: un alumno no puede tener la misma descripción para la misma materia más de una vez.
        unique_together = ('descripcion', 'materia', 'alumno')  
    def __str__(self):
        return f"{self.valor}"