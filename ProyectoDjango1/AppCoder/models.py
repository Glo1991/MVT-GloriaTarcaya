from multiprocessing import parent_process
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class Familia (models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=50)
    fecha_nac=models.DateField()
    edad=models.IntegerField()

class EdadCalculada (models.Model):
    edad_calculada=models.IntegerField()