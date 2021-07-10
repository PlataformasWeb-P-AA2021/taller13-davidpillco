from django.db import models

# Create your models here.

class Edificio(models.Model):
	# Opciones para el tipo de edificio
	opciones_tipo = (
	    ('residencial','Edificio residencial'),
	    ('comercial','Edificio comercial'),
	    )
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	tipo_edificio = models.CharField(max_length=30, \
	        choices=opciones_tipo) 

	def __str__(self):
	    return "%s %s %s %s" % (self.nombre,
		    	self.direccion,
		        self.ciudad,
		        self.tipo_edificio)

	def obtener_cantidad_cuartos(self):
		valor = [t.num_cuartos for t in self.departamentos.all()]
		valor = sum(valor)
		return valor
		
	def obtener_costo_departamento(self):
		valor = [t.costo for t in self.departamentos.all()]
		valor = sum(valor)
		return valor



class Departamento(models.Model):
	nomPropietario = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=100, decimal_places=2)
	num_cuartos = models.IntegerField("Número de cuartos")
	edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
	        related_name="departamentos")

	def __str__(self):
		return "%s %.2f %d %s" % (self.nomPropietario, 
			self.costo,
			self.num_cuartos,
			self.edificio)
