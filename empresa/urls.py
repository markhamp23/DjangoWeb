#urls de Noticies
from django.conf.urls import include,url
from .import views

urlpatterns = [
    url(r'^$',views.dades_empresa),
	url(r'^empresa/',views.dades_empresa),
]