from django.contrib import admin
from .models import Medic, Pacient, Medicament, MedicPacient, Consultatie

@admin.register(Medic)
class MedicAdmin(admin.ModelAdmin):
    list_display = ('MedicID', 'NumeMedic', 'PrenumeMedic', 'Specializare')
    search_fields = ('NumeMedic', 'PrenumeMedic', 'Specializare')

@admin.register(Pacient)
class PacientAdmin(admin.ModelAdmin):
    list_display = ('PacientID', 'NumePacient', 'PrenumePacient', 'CNP', 'Asigurare')
    search_fields = ('NumePacient', 'PrenumePacient', 'CNP')

@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('MedicamentID', 'Denumire')
    search_fields = ('Denumire',)

@admin.register(MedicPacient)
class MedicPacientAdmin(admin.ModelAdmin):
    list_display = ('id', 'medic', 'pacient')
    list_filter = ('medic',)

@admin.register(Consultatie)
class ConsultatieAdmin(admin.ModelAdmin):
    list_display = ('ConsultatieID', 'pacient', 'medic', 'medicament', 'Data', 'Diagnostic')
    list_filter = ('Data', 'medic')
    search_fields = ('pacient__NumePacient', 'Diagnostic')
    date_hierarchy = 'Data'
