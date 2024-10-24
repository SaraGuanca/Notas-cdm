# Generated by Django 5.1.1 on 2024-10-20 22:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

def create_courses(apps, schema_editor):
    Curso = apps.get_model('notascdm_app', 'Curso')
    anio_calendario = 2024

    for anio in range(1, 6):  # Años 1 a 5
        for division in ['a', 'b', 'c', 'd']:  # Divisiones a, b, c, d
            Curso.objects.create(anio=anio, division=division, anio_calendario=anio_calendario)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=8)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('division', models.CharField(max_length=1)),
                ('anio_calendario', models.IntegerField()),
                ('alumnos', models.ManyToManyField(related_name='cursos', to='notascdm_app.alumno')),
                ('materias', models.ManyToManyField(related_name='cursos', to='notascdm_app.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trimestre', models.IntegerField()),
                ('valor', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('descripcion', models.CharField(max_length=30)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='notascdm_app.alumno', verbose_name='notas_alumno')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='notascdm_app.materia', verbose_name='notas_materias')),
            ],
        ),
        migrations.RunPython(create_courses),
    ]
