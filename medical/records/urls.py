from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    # Medic URLs
    path('medic/', views.medic_list, name='medic_list'),
    path('medic/create/', views.medic_create, name='medic_create'),
    path('medic/<int:pk>/update/', views.medic_update, name='medic_update'),
    path('medic/<int:pk>/delete/', views.medic_delete, name='medic_delete'),
    
    # Pacient URLs
    path('pacient/', views.pacient_list, name='pacient_list'),
    path('pacient/create/', views.pacient_create, name='pacient_create'),
    path('pacient/<int:pk>/update/', views.pacient_update, name='pacient_update'),
    path('pacient/<int:pk>/delete/', views.pacient_delete, name='pacient_delete'),
    
    # Medicament URLs
    path('medicament/', views.medicament_list, name='medicament_list'),
    path('medicament/create/', views.medicament_create, name='medicament_create'),
    path('medicament/<int:pk>/update/', views.medicament_update, name='medicament_update'),
    path('medicament/<int:pk>/delete/', views.medicament_delete, name='medicament_delete'),
    
    # Consultatie URLs
    path('consultatie/', views.consultatie_list, name='consultatie_list'),
    path('consultatie/create/', views.consultatie_create, name='consultatie_create'),
    path('consultatie/<int:pk>/update/', views.consultatie_update, name='consultatie_update'),
    path('consultatie/<int:pk>/delete/', views.consultatie_delete, name='consultatie_delete'),
    
    # MedicPacient URLs
    path('medicpacient/', views.medicpacient_list, name='medicpacient_list'),
]