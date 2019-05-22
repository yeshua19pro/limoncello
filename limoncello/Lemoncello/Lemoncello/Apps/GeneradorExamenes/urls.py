from django.urls import path, include
from Lemoncello.Apps.GeneradorExamenes.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls import url

from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('Examenes',  ExamenView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    url(r'^examenes', ExamPDF.as_view(), name='examenes'),   
]
