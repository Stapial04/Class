from django.urls import path
from core.views import doctor_create, doctor_list, doctor_update, doctor_delete
app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('doctor_list/',doctor_list, name='doctor_list'),  # URL para la vista home
    path('doctor_create/',doctor_create, name='doctor_create'),
    path('doctor_update/<int:id>/', doctor_update,name='doctor_update'),
    path('doctor_delete/<int:id>/', doctor_delete,name='doctor_delete'),
]

