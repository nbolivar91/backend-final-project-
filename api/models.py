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
    experiencia = models.IntegerField()



class HabilidadesEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadesEntity
        exclude =()
        
class CiudadEntity(models.Model):
    la_ciudad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.la_ciudad
    
class CiudadEntitySerializer(serializers.ModelSerializer):
    coders = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = CiudadEntity
        exclude =()   
        
class FormadetrabajoEntity(models.Model):
    como_trabaja = models.CharField(max_length=100)
    
    def __str__(self):
        return self.como_trabaja
    
        

class CoderEntity(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, null=True, default=None)
    experiencia = models.IntegerField( null=True, default=None)
    costoXhora = models.FloatField(max_length=50, null=True, default=None)
    cedula = models.IntegerField( unique=True, null=True, default=None)
    biografia = models.CharField(max_length=1000000000, null=True, default=None)
    ciudad = models.ForeignKey(CiudadEntity, on_delete=models.CASCADE, null=True, default=None, related_name="coders")
    forma_trabajo = models.ManyToManyField(FormadetrabajoEntity, related_name="coders")
    
    def __str__(self):
        return self.id
    
class CoderEntitySerializer(serializers.ModelSerializer):
    ciudad = serializers.StringRelatedField(many=False)
    forma_trabajo = serializers.SlugRelatedField(many=True, 
                                                read_only=False, 
                                                slug_field="como_trabaja", 
                                                queryset=FormadetrabajoEntity.objects.all())
    
    class Meta:
        model = CoderEntity
        exclude =()


    
class FormadetrabajoEntitySerializer(serializers.ModelSerializer):
    coders = CoderEntitySerializer(many=True, read_only=True)
    
    class Meta:
        model = FormadetrabajoEntity
        exclude =()  