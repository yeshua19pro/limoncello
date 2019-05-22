from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Lemoncello.Apps.cursos.models import *

@login_required
def perfil(request):
	user_id = request.user.id
	profesor = Profesor.objects.filter(user_id=user_id).values()
	p = profesor[0]

	context = {
		'nombre' : p['nombre'],
		'correo' : p['correo'],
		'usuario': request.user
	}

	return render(request, 'miperfil.html', context)


def misCursos(request):
	user_id = request.user.id
	profesor = Profesor.objects.filter(user_id=user_id).values()
	p = profesor[0]

	cursos = Curso.objects.filter(profesor_id__exact=p['id_profesor'])
	estudiantes = []

	for c in cursos:
		e = Estudiante.objects.filter(curso_id__exact=c.id)
		estudiantes.append(e)

	print(estudiantes)

	context = {
		'cursos' : cursos,
		'estudiantes' : estudiantes[0],	
	}

	if request.method == 'GET':
		print(request.user.id)
	
	return render(request, "misCursos.html", context)

def cursoInfo(request):
	if request.method == 'GET':
		print(request)
	return render(request, "cursoinfo.html", {})

def home(request):
	return render(request, "home.html", {})

def users(request):
	return render(request, "usuarios.html", {})