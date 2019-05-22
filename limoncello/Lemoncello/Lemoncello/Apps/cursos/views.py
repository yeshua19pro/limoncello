from rest_framework import generics, viewsets
from Lemoncello.Apps.cursos.models import *
from Lemoncello.Apps.cursos.forms import *
from Lemoncello.Apps.cursos.serializers import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render


class ProfesorView(viewsets.ModelViewSet):
	queryset = Profesor.objects.all()
	serializer_class = ProfesorSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj

class CursoView(viewsets.ModelViewSet):
	queryset = Curso.objects.all()
	serializer_class = CursoSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj
		

class EstudianteView(viewsets.ModelViewSet):
	queryset = Estudiante.objects.all()
	serializer_class = EstudianteSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj


def cursos(request):
	profesores = Profesor.objects.all()
	estudiantes = Estudiante.objects.all()
	cursos = Curso.objects.all()


	context = {
		'profesores' : profesores,
		'estudiantes' : estudiantes,
		'cursos' : cursos
	}
	return render(request, "cursos.html", context)
	


