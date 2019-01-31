from django.contrib import admin
from django.urls import path, include
from api import views
#example
#urlpatterns = [
#    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
#    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
#]

urlpatterns = [
    path('coder/<int:pk>', views.CoderEntityCrearUpdateDelete.as_view(), name='id-coders'),
    path('coder/', views.CoderEntityList.as_view(), name='all-coders'),
    path('habilidades/<int:fk>', views.HabilidadesEntityCrearUpdateDelete.as_view(), name='id-habilidades'),
    path('habilidades/', views.HabilidadesEntityList.as_view(), name='all-habilidades,'),
    path('formatrabajo/<int:fk>', views.FormadetrabajoEntityCrearUpdateDelete.as_view(), name='id-tipo'),
    path('formatrabajo/', views.FormadetrabajoEntityList.as_view(), name='all-tipo,'),
    path('ciudad/<int:fk>', views.CiudadEntityCrearUpdateDelete.as_view(), name='id-ciudad'),
    path('ciudad/', views.CiudadEntityList.as_view(), name='all-ciudad,'),
    
]