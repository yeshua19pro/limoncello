from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class Profesor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	id_profesor = models.CharField("Identificación", max_length=30, primary_key=True)
	nombre = models.CharField("Nombres y apellidos", max_length=250)
	correo = models.EmailField(max_length=254)

	def __str__(self):
		return self.nombre

class Curso(models.Model):
	curso_choices =(('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),
		('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),
		('16', '16'),('17', '17'),('18', '18'),)
	curso = models.CharField("Curso", choices=curso_choices, max_length=2, default='1')
	horaInicio = models.TimeField("Hora de inicio", default='06:00')
	horaFin = models.TimeField("Hora de finalización", default='08:00')
	intensivo = 'Intensivo'
	semi = 'Semi intensivo'
	regular = 'Regular'
	cat_choices = (
		(intensivo, 'Intensivo'),
		(semi, 'Semi intensivo'),
		(regular, 'Regular')
	)

	catalogo = models.CharField("Catálogo", max_length=100, choices=cat_choices, default=semi)
	dias_choices = (
		('l', 'Lunes'),
		('m', 'Martes'),
		('w', 'Miércoles'),
		('j', 'Jueves'),
		('v', 'Viernes'),
		('s', 'Sábado'),
	)

	dias = MultiSelectField("Días", choices=dias_choices, max_choices=6, default='l,w,v')

	ingles = 'Inglés'
	aleman = 'Alemán'
	frances = 'Francés'
	japones = 'Japonés'
	italiano = 'Italiano'
	idioma_choices = (
		(ingles, 'Inglés'),
		(aleman, 'Alemán'),
		(frances, 'Francés'),
		(japones, 'Japonés'),
		(italiano, 'Italiano'),
		)
	idioma = models.CharField(max_length=50, choices=idioma_choices, default=ingles)
	profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True)
	fechaInicio = models.DateField("Fecha de inicio")
	fechaFin = models.DateField("Fecha de finalización")

	def __int__(self):
		return self.id

class Estudiante(models.Model):
	id_estudiante = models.CharField("Documento de identidad", max_length=30, primary_key=True, unique=True, default="")
	nombre = models.CharField("Nombres y apellidos", max_length=250)
	foto = models.ImageField(upload_to='students',blank=True)
	confidencialidad = models.BooleanField(default=False)
	correo = models.EmailField(max_length=254)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.nombre

