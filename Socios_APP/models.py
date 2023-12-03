from django.db import models
from django.core import validators

# Create your models here.

class Socio(models.Model):

    ESTADO = (
        ('Vigente', 'Vigente'),
        ('Inactivo', 'Inactivo'),
        ('Suspendido', 'Suspendido'),
    )
    SEXO = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Otro', 'Otro'),
    )
    nombre = models.CharField(max_length=80)
    fecha_incorporacion = models.DateField()
    año_nacimiento = models.IntegerField(max_length=4, validators=[validators.MaxValueValidator(2023), validators.MinValueValidator(1900)])
    telefono = models.CharField(max_length=12, validators=[validators.MinLengthValidator(9), validators.MaxLengthValidator(12)])
    email = models.EmailField()
    sexo = models.CharField(max_length=50, choices=SEXO)
    estado = models.CharField(max_length=50, choices=ESTADO)
    observacion = models.CharField(max_length=100, null=True, blank=True)