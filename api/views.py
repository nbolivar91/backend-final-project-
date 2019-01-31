from django.shortcuts import render
import json
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import CoderEntity, CoderEntitySerializer, HabilidadesEntity, HabilidadesEntitySerializer, CiudadEntity, CiudadEntitySerializer, FormadetrabajoEntity, FormadetrabajoEntitySerializer   

#como hacer get, post, delete a codigo limpio python 
# class ContactsView(APIView):
  #  def get(self, request, contact_id=None):
#
 #       if contact_id is not None:
  #          contact = Contact.objects.get(id=contact_id)
   #         serializer = ContactSerializer(contact, many=False)
    #        return Response(serializer.data)
     #   else:
      #      contacts = Contact.objects.all()
       #     serializer = ContactSerializer(contacts, many=True)
    #        return Response(serializer.data)
        
#    def post(self, request):
            
#        serializer = ContactSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_200_OK)
#        else:
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
#    def delete(self, request, contact_id):
#        
#        contact = Contact.objects.get(id=contact_id)
#        contact.delete()
#        
#        return Response(status=status.HTTP_204_NO_CONTENT)

class CoderEntityList(generics.ListCreateAPIView):
    queryset = CoderEntity.objects.all()
    serializer_class = CoderEntitySerializer 
    
class CoderEntityCrearUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CoderEntity.objects.all()
    serializer_class = CoderEntitySerializer
        
class HabilidadesEntityList(generics.ListCreateAPIView):
    queryset = HabilidadesEntity.objects.all()
    serializer_class = HabilidadesEntitySerializer 
    
class HabilidadesEntityCrearUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = HabilidadesEntity.objects.all()
    serializer_class = HabilidadesEntitySerializer
    
class CiudadEntityList(generics.ListCreateAPIView):
    queryset = CiudadEntity.objects.all()
    serializer_class = CiudadEntitySerializer 
    
class CiudadEntityCrearUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = CiudadEntity.objects.all()
    serializer_class = CiudadEntitySerializer    
    
class FormadetrabajoList(generics.ListCreateAPIView):
    queryset = FormadetrabajoEntity.objects.all()
    serializer_class = FormadetrabajoEntitySerializer
    
class FormadetrabajoEntityCrearUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormadetrabajoEntity.objects.all()
    serializer_class = FormadetrabajoEntitySerializer 