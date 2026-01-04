from django import forms
from .models import Medic, Pacient, Medicament, MedicPacient, Consultatie

class MedicForm(forms.ModelForm):
    class Meta:
        model = Medic
        fields = ['NumeMedic', 'PrenumeMedic', 'Specializare']
        widgets = {
            'NumeMedic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}),
            'PrenumeMedic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}),
            'Specializare': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Specializare'}),
        }
        labels = {
            'NumeMedic': 'Nume',
            'PrenumeMedic': 'Prenume',
            'Specializare': 'Specializare',
        }


class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['CNP', 'NumePacient', 'PrenumePacient', 'Adresa', 'Asigurare']
        widgets = {
            'CNP': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '13 digits', 'maxlength': '13'}),
            'NumePacient': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}),
            'PrenumePacient': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}),
            'Adresa': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresa'}),
            'Asigurare': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'CNP': 'CNP',
            'NumePacient': 'Nume',
            'PrenumePacient': 'Prenume',
            'Adresa': 'Adresa',
            'Asigurare': 'Are Asigurare?',
        }


class MedicamentForm(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = ['Denumire']
        widgets = {
            'Denumire': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Denumire medicament'}),
        }
        labels = {
            'Denumire': 'Denumire',
        }


class ConsultatieForm(forms.ModelForm):
    class Meta:
        model = Consultatie
        fields = ['pacient', 'medic', 'medicament', 'Data', 'Diagnostic', 'DozaMedicament']
        widgets = {
            'pacient': forms.Select(attrs={'class': 'form-control'}),
            'medic': forms.Select(attrs={'class': 'form-control'}),
            'medicament': forms.Select(attrs={'class': 'form-control'}),
            'Data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Diagnostic': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Diagnostic'}),
            'DozaMedicament': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 2 pastile/zi'}),
        }
        labels = {
            'pacient': 'Pacient',
            'medic': 'Medic',
            'medicament': 'Medicament',
            'Data': 'Data',
            'Diagnostic': 'Diagnostic',
            'DozaMedicament': 'Doza',
        }


class MedicPacientForm(forms.ModelForm):
    class Meta:
        model = MedicPacient
        fields = ['medic', 'pacient']
        widgets = {
            'medic': forms.Select(attrs={'class': 'form-control'}),
            'pacient': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'medic': 'Medic',
            'pacient': 'Pacient',
        }