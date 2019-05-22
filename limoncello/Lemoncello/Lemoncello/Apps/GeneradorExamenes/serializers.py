from rest_framework import serializers
from Lemoncello.Apps.GeneradorExamenes.models import *

class ExamenSerializer(serializers.ModelSerializer):
	profesor = serializers.HyperlinkedIdentityField(
		view_name = "profesor-detail"
		)
	id_estudiante = serializers.HyperlinkedIdentityField(
		view_name = "estudiante-detail"
		)
	id_curso = serializers.HyperlinkedIdentityField(
		view_name = "curso-detail"
		)

	class Meta:
		model = Examen
		fields = ('serial', 'fecha','tipoexamen', 'id_curso',
			'id_estudiante', 'profesor')
