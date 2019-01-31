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
]