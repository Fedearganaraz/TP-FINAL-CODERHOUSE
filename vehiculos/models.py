from django.db import models


# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=70)
    fecha_publicacion = models.DateField (null=True)




















class carros(models.Model):
    
    marca = models.CharField( max_length = 20 )
    
    color = models.CharField( max_length = 20)
    
    cantidad_pasajeros = models.IntegerField()
    
    fecha_salida = models.DateField()

    def __str__(self):
        return self.marca

    
class motos(models.Model):

    marca = models.CharField( max_length = 20 )
    
    color = models.CharField( max_length = 20)
    
    cantidad_pasajeros = models.IntegerField()
    
    fecha_salida = models.DateField()

    def __str__(self):
        return self.marca