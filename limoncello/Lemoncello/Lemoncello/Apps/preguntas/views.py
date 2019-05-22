from rest_framework import generics, viewsets
from Lemoncello.Apps.preguntas.models import *
from Lemoncello.Apps.preguntas.forms import *
from Lemoncello.Apps.preguntas.serializers import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render




class PreguntaView(viewsets.ModelViewSet):
	queryset = Pregunta.objects.all()
	serializer_class = PreguntaSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class RespuestaView(viewsets.ModelViewSet):
	queryset = Respuesta.objects.all()
	serializer_class = RespuestaSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class ContenidoView(viewsets.ModelViewSet):
	queryset = Contenido.objects.all()
	serializer_class = ContenidoSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class SeccionView(viewsets.ModelViewSet):
	queryset = Seccion.objects.all()
	serializer_class = SeccionSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class ListeningView(viewsets.ModelViewSet):
	queryset = Listening.objects.all()
	serializer_class = ListeningSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class ReadingView(viewsets.ModelViewSet):
	queryset = Reading.objects.all()
	serializer_class = ReadingSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class StrctrView(viewsets.ModelViewSet):
	queryset = Strctr.objects.all()
	serializer_class = StrctrSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class WritingView(viewsets.ModelViewSet):
	queryset = Writing.objects.all()
	serializer_class = WritingSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj



def preguntasView(request):
	pregunta = Pregunta.objects.all()
	respuestas = Respuesta.objects.all()
	contenidos = Contenido.objects.all()
	wrt = Writing.objects.all()

	context = {
		'preguntas' : pregunta,
		'respuestas' : respuestas,
		'contenidos' : contenidos,
		'wrt' : wrt
	}
	return render(request, "preguntas.html", context)