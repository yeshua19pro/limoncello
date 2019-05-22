
from django.db import models

class Contenido(models.Model):
	l = 'Listening'
	r = 'Reading'
	s = 'Structure-Vocabulary'
	w = 'Writing'
	tipo_choices = (
		    (l, 'Listening'),
		    (r, 'Reading'),
		    (s, 'Structure-Vocabulary'),
		    (w, 'Writing'),
	)

	tipo = models.CharField(max_length=100, choices = tipo_choices, default = l)
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
	curso = models.PositiveIntegerField()
	enunciado = models.CharField(max_length=3000, default='', blank=True)
	dificultad = models.PositiveIntegerField(default=1)
	imagen = models.ImageField(upload_to='img', blank=True)
	standard = models.CharField(max_length=1000, default='', blank=True)



class Seccion(models.Model):
	enunciado = models.CharField(max_length=3000)
	standard = models.CharField(max_length=1000, default='', blank=True)
	texto = models.CharField(max_length=3000, blank=True)
	image = models.ImageField(upload_to="img", blank=True)
	contenido = models.ForeignKey(
		Contenido,
		on_delete=models.CASCADE,
		null=True
		)

class Pregunta(models.Model):
	l = 'Listening'
	r = 'Reading'
	s = 'Structure-Vocabulary'
	w = 'Writing'
	tipo_choices = (
		    (l, 'Listening'),
		    (r, 'Reading'),
		    (s, 'Structure-Vocabulary'),
		    (w, 'Writing'),
	)

	tipo = models.CharField(max_length=100, choices = tipo_choices, default = l)
	enunciado = models.CharField(max_length=3000, blank=True)
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
	curso = models.PositiveIntegerField()
	contenido = models.ForeignKey(
		Contenido,
		on_delete=models.CASCADE,
		null=True
		)
	seccion = models.ForeignKey(
		Seccion,
		on_delete=models.CASCADE,
		null=True,
		blank=True
		)

class Respuesta(models.Model):
	enunciado = models.CharField(max_length=3000)
	es_correcta = models.BooleanField()
	pregunta = models.ForeignKey(
		Pregunta, 
		on_delete=models.CASCADE,
		null=True
		)

class Listening(models.Model):
	tipo = models.CharField(max_length=50, default="Listening", editable=False)
	direccion_audio = models.CharField("Dirección del audio", max_length=500)
	texto_audio = models.CharField("Transcripción del audio", max_length=3000)	
	contenido = models.ForeignKey(
		Contenido,
		on_delete=models.CASCADE,
		null=True
		)

class Reading(models.Model):
	tipo = models.CharField(max_length=50, default="Reading", editable=False)
	texto_lectura = models.CharField("Texto", max_length=3000)
	contenido = models.ForeignKey(
		Contenido,
		on_delete=models.CASCADE,
		null=True
		)

class Strctr(models.Model):
	tipo = models.CharField(max_length=50, default="Structure-Vocabulary", editable=False)
	contenido = models.ForeignKey(
		Contenido,
		on_delete=models.CASCADE,
		null=True
		)

class Writing(models.Model):
	tipo = models.CharField(max_length=50, default="Writing", editable=False)
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
	curso = models.PositiveIntegerField()
	enunciado = models.CharField(max_length=3000)
	dificultad = models.PositiveIntegerField(default=1)
	standard = models.CharField(max_length=1000, default='', blank=True)