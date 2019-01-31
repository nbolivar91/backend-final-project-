from rest_framework import serializers
from django.db import models

# Create your models here. (example) 
# class Contact(models.Model):
#    first_name = models.CharField(max_length=50)
#    last_name = models.CharField(max_length=50)
    

#class ContactSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Contact
#        exclude = ()
class HabilidadesEntity(models.Model):
    lenguaje = models.CharField(max_length=50)
    experiencia = models.IntegerField (max_length=2)

class HabilidadesEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadesEntity
        exclude =()
        
class CiudadEntity(models.Model):
    la_ciudad = models.CharField(max_length=50)
    
class CiudadEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CiudadEntity
        exclude =()   
        
class FormadetrabajoEntity(models.Model):
    como_trabaja = models.CharField(max_length=100)
    
class FormadetrabajoEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FormadetrabajoEntity
        exclude =()  
        
class CoderEntity(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, null=True, default=None)
    experiencia = models.IntegerField(max_length=2, null=True, default=None)
    costoXhora = models.FloatField(max_length=50, null=True, default=None)
    cedula = models.IntegerField(max_length=30, unique=True, null=True, default=None)
    biografia = models.CharField(max_length=1000000000, null=True, default=None)
    
class CoderEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoderEntity
        exclude =()
 

    
    