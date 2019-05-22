from rest_framework import generics, viewsets
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView
from django.core.files import File

from Lemoncello.Apps.GeneradorExamenes.models import *
from Lemoncello.Apps.GeneradorExamenes.forms import *
from Lemoncello.Apps.GeneradorExamenes.serializers import *
from Lemoncello.Apps.GeneradorExamenes.utils import *

from Lemoncello.Apps.preguntas.forms import *
from Lemoncello.Apps.preguntas.models import *
from Lemoncello.Apps.cursos.models import *

import random



class ExamenView(viewsets.ModelViewSet):
	queryset = Examen.objects.all()
	serializer_class = ExamenSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
			)
		return obj


class ExamPDF(TemplateView):


	def get(self, request):
		form = ExamForm()
		examen = Examen.objects.all()
		context = {
			'form': form,
			'examen' : examen
		}
		return render(request, 'exams.html', context)


	def post(self, request):
		form = ExamForm(request.POST)
		
		examen = Examen.objects.all()
		
		if form.is_valid():
			fecha = form.cleaned_data['fecha']
			tipo = form.cleaned_data['tipo']
			curso = form.cleaned_data['curso']
			dificultad = form.cleaned_data['dificultad']
			lstng = form.cleaned_data['lstng']
			lisnum = form.cleaned_data['lisnum']
			read = form.cleaned_data['read']
			readnum = form.cleaned_data['readnum']
			strc = form.cleaned_data['strc']
			strcnum = form.cleaned_data['strcnum']
			wrt = form.cleaned_data['wrt']

			context2 = {
				'fecha' : fecha,
				'tipo' : tipo,
				'curso' : curso,
				'dificultad' : dificultad,
				'lstng' : lstng,
				'lisnum' : lisnum,
				'read' : read,
				'readnum' : readnum,
				'strc' : strc,
				'strcnum' : strcnum,
				'wrt' : wrt
			}
			form = ExamForm()
			buildExam(context2)
		else:
			form = ExamForm()
		
		context = {
			'form' : form,
			'examen' : examen
		}

		return render(request, 'exams.html', context)


def buildExam(params):
	cursoObj = params['curso']
	queryset = Curso.objects.filter(id__exact=cursoObj).values()
	cursoInfo = queryset[0]
	dias = cursoInfo['dias']

	schedule = ""
	for d in dias:
		schedule += d + " "

	profesor = cursoInfo['profesor_id']
	profesorObj = Profesor.objects.filter(id_profesor__exact=profesor).values()
	profesorVal = profesorObj[0]

	estudiantesObj = Estudiante.objects.filter(curso__exact=cursoObj).values()

	contL = None
	contR = None
	contS = None

	modL = None
	modR = None
	modS = None

	pl = None
	pr = None
	ps = None

	idioma = cursoInfo['idioma']

	if params['lstng']:
		contL = getContent(params['dificultad'], idioma, cursoInfo['curso'], 'Listening')
		if contL: 
			idcontent = contL['id']
			modL = getModule(idcontent, Listening)
			pl = getQuestions(idcontent)
		else: 
			print('No hay contenidos Listening')

	if params['read']:
		contR = getContent(params['dificultad'], idioma, cursoInfo['curso'], 'Reading')
		if contR:
			idcontent = contR['id']
			modR = getModule(idcontent, Reading)
			pR = getQuestions(idcontent)
		else: 
			print('No hay contenidos Reading')

	if params['strc']:
		contS = getContent(params['dificultad'], idioma, cursoInfo['curso'], 'Strctr')
		if contS:
			idcontent = contS['id']
			modS = getModule(idcontent, Strctr)
			ps = getQuestions(idcontent)
		else: 
			print('No hay contenidos Structure')

	for e in estudiantesObj:
		serial = SerialCreation()
		pdfPath = serial + ".pdf"

		wrt = Writing.objects.filter(dificultad=params['dificultad'],
		 curso=cursoInfo['curso'], idioma=idioma)
		randomWriting = random.choices(wrt)

		print(contL)

		contenidoExamen = {
			'title' : "ADULT " + params['tipo'] + " WRITTEN TEST LANGUAGE  CENTER",
			'serial' : serial,
			'name' : e['nombre'],
			'date' : params['fecha'],
			'schedule' : schedule,
			'teacher' : profesorVal['nombre'],
			'course' : cursoInfo['curso'],
			'contL' : contL,
			'contS' : contS,
			'contR' : contR,
			'modL' : modL,
			'modS' : modS,
			'modR' : modR,
			'wrt' : randomWriting,
			'pl' : pl,
			'pr' : pr,
			'ps' : ps
		}

		#print(contenidoExamen)

		renderToPdf(contenidoExamen, pdfPath)
		file = open(pdfPath, "r")
		pdfExam = File(file)

		examen = Examen.objects.create(
			fecha = params['fecha'],
			tipoexamen = params['tipo'],
			id_estudiante = e['id_estudiante'],
			nombre = e['nombre'],
			id_curso = cursoInfo['id'],
			profesor = profesorVal['nombre'],
			serial = serial,
			pdf = pdfExam
		)
		examen.save()
		file.close()


def getContent(dificultad, idioma, curso, tipo):
	contenidos = Contenido.objects.filter(tipo=tipo,
		 dificultad=dificultad, idioma=idioma, curso=curso).values()
	print(contenidos)
	if contenidos:
		contenido = random.choices(contenidos)
		return contenido[0]
	else:
		return None
	

def getSeccions(idcontent):
	return Seccion.objects.filter(contenido__exact=idcontent).values()

def getModule(idcontent, modulo):
	return modulo.objects.filter(contenido__exact=idcontent).values()

def getQuestions(idcontent):
	return Pregunta.objects.filter(contenido__exact=idcontent).values()






		


