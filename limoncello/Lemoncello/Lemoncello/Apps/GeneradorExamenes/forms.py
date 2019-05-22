from django import forms
from Lemoncello.Apps.GeneradorExamenes.models import *
from Lemoncello.Apps.cursos.models import *


class ExamForm(forms.Form):
	fecha = forms.DateField(widget=forms.SelectDateWidget())
	tipo_c = (('MIDTERM', 'MIDTERM'), ('FINAL', 'FINAL'))
	tipo = forms.ChoiceField(choices = tipo_c, label="Tipo", 
		initial='Parcial', widget=forms.Select())
	curso = forms.ModelChoiceField(queryset=Curso.objects.all())

	dificultad = forms.IntegerField(label='Dificultad', min_value=1, max_value=3)

	lstng = forms.BooleanField(label='Listening')
	lisnum = forms.IntegerField(label='Cantidad de secciones', min_value=1, max_value=2)

	read = forms.BooleanField(label='Reading')
	readnum = forms.IntegerField(label='Cantidad de secciones', min_value=1, max_value=2)

	strc = forms.BooleanField(label='Structure')
	strcnum = forms.IntegerField(label='Cantidad de secciones', min_value=1, max_value=3)

	wrt = forms.BooleanField(label='Writing')