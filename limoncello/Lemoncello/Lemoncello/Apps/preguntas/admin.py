from django.contrib import admin
from django.contrib.admin import AdminSite
from Lemoncello.Apps.preguntas.models import *

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='Preguntas')

admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Contenido)
admin.site.register(Seccion)
admin.site.register(Listening)
admin.site.register(Reading)
admin.site.register(Strctr)
admin.site.register(Writing)
