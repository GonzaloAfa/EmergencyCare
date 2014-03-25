from django.db import models

# Create your models here.

class Sexo(models.Model):
	tipo = models.CharField(max_length=10)
	def __unicode__(self):
		return self.tipo


class Causa (models.Model):
	causa  = models.CharField(max_length=30)
	def __unicode__(self):
		return self.causa 

class TipoMovil (models.Model):
	tipo_movil = models.CharField(max_length=30)
	def __unicode__(self):
		return self.tipo_movil

class EstadoFicha (models.Model):
	estado_ficha = models.CharField(max_length=15)
	def __unicode__(self):
		return self.estado_ficha

class Glasgow (models.Model):
	glasgow = models.CharField(max_length=10)




class Ficha (models.Model):

	date_start 		= models.DateTimeField(auto_now=True)
	estado_ficha   	= models.ForeignKey(EstadoFicha)

	#Datos del paciente
	nombre		= models.CharField(max_length=60)
	apellido 	= models.CharField(max_length=60)
	rut			= models.CharField(max_length=12)
	edad		= models.IntegerField()
	sexo 		= models.ForeignKey(Sexo)
	diagnostico	= models.TextField()

	
	#Datos del traslado
	responsable 	= models.CharField(max_length=60)
	telefono		= models.CharField(max_length=13)
	origen			= models.CharField(max_length=120)
	medico_derivador= models.CharField(max_length=60)
	destino			= models.CharField(max_length=120)
	medico_receptor	= models.CharField(max_length=60)
	causa			= models.ForeignKey(Causa)


	#Datos gravedad del paciente
	tipo_movil 		= models.ForeignKey(TipoMovil)

	#datos internos que despues se modifican
	km_inicio		= models.IntegerField(blank=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	km_termino		= models.IntegerField(blank=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_inicio		= models.CharField(max_length=5, blank=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_llegada	= models.CharField(max_length=5, blank=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	
	hora_QTH_inicio	= models.CharField(max_length=5, blank=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_QTH_final	= models.CharField(max_length=5, blank=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")


	# requerimientos del paciente
	
	# Oxigenoterapia -> cantidad
	# ventilacion mecanica
	# Via Venosa 
	# via venosa central
	# via venosa periferica
	# BIC (Bomba de infusion continua)
	# Monitorizacion
	# marcapaso
	# otro -> 

	
	# Condicion
	# hemodinamia estable
	# hemodinamia inestable
	# glasgow
	# > 15
	# > 9 - 14
	# > 0 - 8


	def __unicode__(self):
		return self.nombre +" "+ self.apellido







