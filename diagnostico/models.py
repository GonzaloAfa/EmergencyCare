from django.db import models



CHOICES_OXIGENOTERAPIA = (
	(1, 'Naricera'),
	(2, 'Mascarilla Fio2 35-50%'),
	(3, 'Ventilacion Invasiva | No Invasiva'),
)

CHOICES_ACCESO = (
	(1, 'Periferico'),
	(2, 'Central'),
	)

CHOICES_HEMODINAMIA =(
	(1, 'Estable'),
	(2, 'Inestable')
	)

CHOICES_VENTILATORIO = (
	(1, 'Eupneico'),
	(2, 'Alterado'),
	)
	
CHOICES_GLASGOW = (
	(1, '14 - 15'),
	(2, '9 - 13'),
	(3, '0 - 8'),
	)


class Requerimientos(models.Model):

	monitorizacion 			= models.BooleanField(default=None)
	ventilacion_mecanica 	= models.BooleanField(default=None)	
	inmovilizacion			= models.BooleanField(default=None)
	marcapaso				= models.BooleanField(default=None)

	BIC 					= models.CharField(max_length=20, blank=True)
	oxigenoterapia 			= models.CharField(max_length=20, choices=CHOICES_OXIGENOTERAPIA, blank=True);
	acceso_vascular			= models.CharField(max_length=20, choices=CHOICES_ACCESO, blank=True)

#Condicion Paciente
	hemodinamia				= models.CharField(max_length=20, choices=CHOICES_HEMODINAMIA, blank=True)
	ventilatorio			= models.CharField(max_length=20, choices=CHOICES_VENTILATORIO, blank=True)
	glasgow					= models.CharField(max_length=20, choices=CHOICES_GLASGOW, blank=True)
