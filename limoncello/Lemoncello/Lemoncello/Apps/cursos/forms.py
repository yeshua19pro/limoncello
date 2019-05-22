from django import forms
from Lemoncello.Apps.cursos.models import *

class ProfesorForm(forms.ModelForm):
	class Meta:
		model = Profesor
		fields = ['id_profesor', 'nombre', 'correo']

class EstudianteForm(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = ['id_estudiante','nombre', 'correo', 'curso', 'confidencialidad', 'foto']

class CursoForm(forms.ModelForm):
	class Meta:
		model = Curso
		fields = ['curso', 'horaInicio', 'horaFin',
		 'catalogo', 'dias', 'idioma', 'profesor', 'fechaInicio', 'fechaFin']