from django import forms
from Lemoncello.Apps.preguntas.models import *

class PreguntaForm(forms.ModelForm):
	class Meta:
		model = Pregunta
		fields = ['tipo', 'idioma', 'enunciado', 'contenido', 'seccion', 'id']

class RespuestaForm(forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = ['enunciado','es_correcta', 'pregunta']

class ContenidoForm(forms.ModelForm):
	class Meta:
		model = Contenido
		fields = ['enunciado','tipo', 'idioma', 'curso', 'id']
