from django.db import models
from django.utils.translation import ugettext_lazy as _



ENLISTADO  	= '1'
ENCURSO 	= '2'
FINALIZADO 	= '3'
ANULADO 	= '4'


CHOICE_SOLICITUD=(
	('1', 'Programada'),
	('2', 'De inmediato'),	
	)


CHOICES_CAUSA = (
    ('1', 'Examen'),
    ('2', 'Traslado'),
    ('3', 'Derivacion'),
    ('4', 'Domicilio'),
)


CHOICES_STATUS = (
    (ENLISTADO	, 'En lista'),
    (ENCURSO 	, 'En Curso'),
    (FINALIZADO , 'Finalizado'),
    (ANULADO 	, 'Anulado'),
)

CHOICES_MOVIL = (
	('Normal', 'Complejidad Baja'),
	('Medio' , 'Complejidad Mediana '),
	('Alto'  , 'Complejidad Alta '),
)


SALIRBASE		= '1'
CONTACTO 		= '2'
INICIOTRASLADO 	= '3'
FINTRASLADO		= '4'
ENTREGA 		= '5'

CHOICES_TRASLADO = (
	(SALIRBASE 		,'Salir de la base'),
	(CONTACTO 		,'Contacto con paciente'),
	(INICIOTRASLADO ,'Inicio Traslado'),
	(FINTRASLADO 	,'Finaliza Traslado'),
	(ENTREGA 		,'Entrega del paciente'),
	)


class Movil(models.Model):
	apodo 				= models.CharField(max_length=50)
	patente				= models.CharField(max_length=6)

	def __unicode__(self):
		return self.apodo		


class Ficha (models.Model):
	
	#Datos del paciente
	nombre				= models.CharField(max_length=60)
	apellido 			= models.CharField(max_length=60)
	rut					= models.CharField(max_length=12)
	edad				= models.IntegerField()
	causa  				= models.CharField(max_length=30,choices=CHOICES_CAUSA)
	diagnostico			= models.TextField(blank=True, null=True)
	observacion			= models.TextField(blank=True, null=True)	


	#Datos gravedad del paciente
	tipo_movil 			= models.CharField(max_length=30, choices=CHOICES_MOVIL)
	

	#Datos del traslado
	responsable 		= models.CharField(max_length=60)
	telefono			= models.CharField(max_length=13)
	origen				= models.CharField(max_length=120)
	medico_derivador 	= models.CharField(max_length=60)
	destino				= models.CharField(max_length=120)
	medico_receptor		= models.CharField(max_length=60)


	def __unicode__(self):
		return self.nombre +" "+ self.apellido


class Traslado(models.Model):

	movil 				= models.ForeignKey(Movil)
	estado_traslado		= models.CharField(max_length=20,choices=CHOICES_TRASLADO)

	#Datos internos que despues se modifican
	km_inicio			= models.PositiveIntegerField(blank=True, null=True)
	km_termino			= models.PositiveIntegerField(blank=True, null=True)

	contacto_paciente	= models.DateTimeField(max_length=10, blank=True, null=True)
	inicio_traslado		= models.DateTimeField(max_length=10, blank=True, null=True)
	
	fin_traslado 		= models.DateTimeField(max_length=10, blank=True, null=True)
	entrega_paciente	= models.DateTimeField(max_length=10, blank=True, null=True)


	def __unicode__(self):
		return self.id_ficha


class Servicio(models.Model):
	
	estado_ficha 		= models.CharField(max_length=30, choices=CHOICES_STATUS)
	solicitud 			= models.CharField(_('Tipo de solicitud'),max_length=30, choices=CHOICE_SOLICITUD)

	date_start 			= models.DateTimeField(auto_now=True)

	# si es programada, se almacenara informacion en este lugar.
	hora_programada 	= models.DateTimeField(max_length=20, blank=True, null=True)                                                                                                                                                                                                                                                         

	ficha 				= models.ForeignKey(Ficha)
	traslado  			= models.ForeignKey(Traslado)

	def __unicode__(self):
		return self.estado_ficha+ " - "+self.ficha.nombre + " " + self.ficha.apellido
