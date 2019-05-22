from Lemoncello.Apps.cursos.models import *
from rest_framework import serializers

class ProfesorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profesor
		fields = ('id_profesor', 'nombre', 'correo')

class CursoSerializer(serializers.ModelSerializer):
	profesor = serializers.HyperlinkedIdentityField(
		view_name = "profesor-detail"
		)

	class Meta:
		model = Curso
		fields = ('curso','horaInicio', 'horaFin', 'catalogo', 'dias', 'idioma', 'profesor', 'fechaInicio', 'fechaFin')

class EstudianteSerializer(serializers.ModelSerializer):
	curso = serializers.HyperlinkedIdentityField(
		view_name = 'curso-detail'
		)
	class Meta:
		model = Estudiante
		fields = ('id_estudiante', 'nombre', 'curso', 'foto', 'confidencialidad', 'correo')