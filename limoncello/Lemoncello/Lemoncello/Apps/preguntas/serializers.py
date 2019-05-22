from Lemoncello.Apps.preguntas.models import *
from rest_framework import serializers

class ContenidoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contenido
		fields = ('tipo','curso', 'idioma', 'dificultad', 'enunciado')

class SeccionSerializer(serializers.ModelSerializer):
	contenido = serializers.HyperlinkedIdentityField(
		view_name = "contenido-detail"
		)
	class Meta:
		model = Seccion
		fields = ('enunciado', 'texto', 'image', 'contenido')


class PreguntaSerializer(serializers.ModelSerializer):
	contenido = serializers.HyperlinkedIdentityField(
		view_name = "contenido-detail"
		)
	seccion = serializers.HyperlinkedIdentityField(
		view_name = "seccion-detail"
		)
	class Meta:
		model = Pregunta
		fields = ('tipo', 'idioma', 'curso', 'enunciado', 'contenido', 'seccion')


class RespuestaSerializer(serializers.ModelSerializer):
	respuesta = serializers.HyperlinkedIdentityField(
		view_name = "respuesta-detail"
		)
	class Meta:
		model = Respuesta
		fields = ('enunciado', 'respuesta', 'es_correcta')


class ListeningSerializer(serializers.ModelSerializer):
	contenido = serializers.HyperlinkedIdentityField(
		view_name = "contenido-detail"
		)
	class Meta:
		model = Listening
		fields = ('tipo','direccion_audio', 'texto_audio', 'contenido')

class ReadingSerializer(serializers.ModelSerializer):
	contenido = serializers.HyperlinkedIdentityField(
		view_name = "contenido-detail"
		)
	class Meta:
		model = Reading
		fields = ('tipo', 'texto_lectura', 'contenido')

class StrctrSerializer(serializers.ModelSerializer):
	contenido = serializers.HyperlinkedIdentityField(
		view_name = "contenido-detail"
		)
	class Meta:
		model = Strctr
		fields = ('tipo', 'contenido')

class WritingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Writing
		fields = ('tipo','idioma', 'curso', 'enunciado')