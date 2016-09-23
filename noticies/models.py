from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
	titol_post = models.CharField('titol de la noticia',max_length=100)
	text_post = models.TextField('Contingut de la noticia')
	autor_post = models.ForeignKey('auth.User')
	creacio_post = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return u'%s' % (self.titol_post)	
	class Meta:
		ordering = ['titol_post']


class categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True)
	titol_categoria = models.CharField('Titol de la categoria',max_length=40)


	def __unicode__(self):
		return u'%s' % (self.titol_categoria)	
	class Meta:
		ordering = ['titol_categoria']		