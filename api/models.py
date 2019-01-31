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

class CoderEntity(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
class CoderEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoderEntity
        exclude =()