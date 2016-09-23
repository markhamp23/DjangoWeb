#urls de Noticies
from django.conf.urls import include,url
from .import views

urlpatterns = [
    url(r'^$',views.pag_ini),
	url(r'^inici/$',views.pag_ini),
]