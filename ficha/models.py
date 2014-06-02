from django.db import models


CHOICES_CAUSA = (
    ('Examen', 'Examen'),
    ('Derivacion', 'Derivacion'),
    ('Domicilio', 'Domicilio'),
)

PROGRAMADO  = 'Programado'
PROCESO 	= 'En Proceso'
ARCHIVO 	= 'Archivado'

CHOICES_ESTADO = (
    (PROGRAMADO, 	'Programado'),
    (PROCESO, 		'En Proceso'),
    (ARCHIVO, 		'Archivado'),
)

CHOICES_MOVIL = (
	('Normal','Basico'),
	('Medio','Mediana Complejidad'),
	('Alto','Alta Complejidad'),
)

CHOICES_GENERO =(
	('M','Masculino'),
	('F','Femenino'),
)






class Ficha (models.Model):

	
	estado_ficha = models.CharField(max_length=30,choices=CHOICES_ESTADO)
	
	#Datos del paciente
	nombre		= models.CharField(max_length=60)
	apellido 	= models.CharField(max_length=60)
	rut			= models.CharField(max_length=12)
	edad		= models.IntegerField()
	sexo 		= models.CharField(max_length=10, choices=CHOICES_GENERO)
	
	diagnostico	= models.TextField()

	
	#Datos del traslado
	responsable 	= models.CharField(max_length=60)
	telefono		= models.CharField(max_length=13)
	origen			= models.CharField(max_length=120)
	medico_derivador= models.CharField(max_length=60)
	destino			= models.CharField(max_length=120)
	medico_receptor	= models.CharField(max_length=60)
	causa  			= models.CharField(max_length=30,choices=CHOICES_CAUSA)
	

	#Datos gravedad del paciente
	tipo_movil 		= models.CharField(max_length=30, choices=CHOICES_MOVIL)
	

	date_start 			= models.DateTimeField(auto_now=True)
	hora_programada 	= models.DateTimeField(max_length=10, blank=True, null=True)

	#datos internos que despues se modifican
	km_inicio			= models.PositiveIntegerField(blank=True, null=True)
	km_termino			= models.PositiveIntegerField(blank=True, null=True)

	hora_inicio_Espera	= models.CharField(max_length=5, blank=True, null=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_llegada_Espera	= models.CharField(max_length=5, blank=True, null=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	
	hora_QTH_inicio		= models.CharField(max_length=5, blank=True, null=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")
	hora_QTH_final		= models.CharField(max_length=5, blank=True, null=True, help_text="Ingrese en formano 24 hrs. Ejemplo 22:00")


	def __unicode__(self):
		return self.nombre +" "+ self.apellido



CHOICES_OXIGENOTERAPIA = (
	('1','1'),
	('2','2'),
	('3','3'),
)

CHOICES_ACCESO = (
	('1','Periferico'),
	('2','Central'),
	)

CHOICES_HEMODINAMIA =(
	('1','Estable'),
	('2', 'Inestable')
	)

CHOICES_VENTILATORIO = (
	('1','Eupneico'),
	('2','Alterado'),
	)
	
CHOICES_GLASGOW = (
	('1', '0 - 8'),
	('2', '9 - 14'),
	('3', 'Mayor a 14'),
	)

class Requerimientos(models.Model):

	ficha 					= models.CharField(max_length=20)
	tipo_movil				= models.CharField(max_length=20, choices=CHOICES_MOVIL)

	monitorizacion 			= models.BooleanField(blank=True)
	ventilacion_mecanica 	= models.BooleanField(blank=True)	
	inmovilacion			= models.BooleanField(blank=True)
	marcapaso				= models.BooleanField(blank=True)

	BIC 					= models.CharField(max_length=20, blank=True)
	oxigenoterapia 			= models.CharField(max_length=20, choices=CHOICES_OXIGENOTERAPIA, blank=True);
	acceso_vascular			= models.CharField(max_length=20, choices=CHOICES_ACCESO, blank=True)

#Condicion Paciente
	hemodinamia				= models.CharField(max_length=20, choices=CHOICES_HEMODINAMIA, blank=True)
	ventilatorio			= models.CharField(max_length=20, choices=CHOICES_VENTILATORIO, blank=True)
	glasgow					= models.CharField(max_length=20, choices=CHOICES_GLASGOW, blank=True)


class Tripulacion (models.Model):
	conductor	=	models.CharField(max_length=30)
	tens 		= 	models.CharField(max_length=20)
	enfermera	=	models.CharField(max_length=30)
	medico 		= 	models.CharField(max_length=30)