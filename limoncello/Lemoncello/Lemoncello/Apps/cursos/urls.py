from django.urls import path, include
from Lemoncello.Apps.cursos.views import *
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('Profesores',  ProfesorView)
router.register('Cursos',  CursoView)
router.register('Estudiantes',  EstudianteView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    url(r'^cursos', cursos, name='cursos'),
]
