import random
from django.db import models
from Lemoncello.Apps.cursos.models import *
from Lemoncello.Apps.preguntas.models import *


class Examen(models.Model):

    def SerialCreation(b=None): #Creacion de Metodo SerialCreation
        lnlist=[]
        string=""
        for j in range(16):#Numero de caracteres en el serial
            serialnumber = random.choice(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                        "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
            lnlist.append(serialnumber)
        x= string.join(lnlist)
        return x

    fecha = models.DateField()
    tipo = (('M', 'MIDTERM'), ('F', 'FINAL'))
    tipoexamen = models.CharField(max_length=1, choices=tipo)
    id_estudiante = models.CharField(max_length=300, default='')
    nombre = models.CharField(max_length=300, default='')
    id_curso = models.CharField(max_length=300, default=0)
    profesor = models.CharField(max_length=300, default='')
    serial = models.CharField(max_length=16, default=SerialCreation(), editable=False)
    pdf = models.FileField(upload_to='pdf', default='', blank=True)

    def __str__(self):
        return self.tipoexamen