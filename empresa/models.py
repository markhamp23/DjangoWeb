from __future__ import unicode_literals

from django.db import models

# Create your models here.
#Dades empresa
class empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nom_empresa = models.CharField(max_length=40)
    mail_empresa = models.EmailField(max_length=80)
    tlf_empresa = models.CharField(max_length=9)
    adr_empresa = models.CharField(max_length=5)
    cp_empresa = models.CharField(max_length=5)
    #logo_empresa = models.CharField(upload_to='uploads',verbose_name='Empresa_Imatges')
  
    def __unicode__(self):
    	return u'%s' % (self.nom_empresa)

	class Meta:
		ordering = ['nom_empresa']

class centre(models.Model):
    id_centre = models.AutoField(primary_key=True)
    cit_centre = models.CharField(max_length=20)
    cp_centre = models.CharField(max_length=5)
    mail_centre = models.EmailField(max_length=80)
    cod_empresa = models.ForeignKey(empresa,related_name='empresa')		

    def __unicode__(self):
    	return u'%s' % (self.nom_centre)

	class Meta:
		ordering = ['nom_centre']
