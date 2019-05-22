from django.urls import path, include
from Lemoncello.Apps.preguntas.views import *
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register('Contenidos',  ContenidoView)
router.register('Secciones',  SeccionView)
router.register('Preguntas',  PreguntaView)
router.register('Respuestas',  RespuestaView)
router.register('Listenings',  ListeningView)
router.register('Readings',  ReadingView)
router.register('Structrures',  StrctrView)
router.register('Writings',  WritingView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    url(r'^preguntas', preguntasView, name='Bancopreguntas'),
]
