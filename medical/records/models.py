from django.db import models
from django.core.validators import RegexValidator

class Medic(models.Model):
    MedicID = models.AutoField(primary_key=True)
    NumeMedic = models.CharField(max_length=100)
    PrenumeMedic = models.CharField(max_length=100)
    Specializare = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'medic'
        verbose_name_plural = 'Medici'
    
    def __str__(self):
        return f"Dr. {self.NumeMedic} {self.PrenumeMedic}"


class Pacient(models.Model):
    PacientID = models.AutoField(primary_key=True)
    
    # CNP validator: exactly 13 digits
    cnp_validator = RegexValidator(
        regex=r'^\d{13}$',
        message='CNP must be exactly 13 digits'
    )
    CNP = models.CharField(
        max_length=13, 
        unique=True, 
        validators=[cnp_validator]
    )
    
    NumePacient = models.CharField(max_length=100)
    PrenumePacient = models.CharField(max_length=100)
    Adresa = models.TextField(blank=True, null=True)
    Asigurare = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'pacient'
        verbose_name_plural = 'Pacienti'
    
    def __str__(self):
        return f"{self.NumePacient} {self.PrenumePacient} (CNP: {self.CNP})"


class Medicament(models.Model):
    MedicamentID = models.AutoField(primary_key=True)
    Denumire = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'medicament'
        verbose_name_plural = 'Medicamente'
    
    def __str__(self):
        return self.Denumire


class MedicPacient(models.Model):
    """Junction table for Many-to-Many relationship between Medic and Pacient"""
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'medic_pacient'
        unique_together = ('medic', 'pacient')
        verbose_name_plural = 'Medic-Pacient Relations'
    
    def __str__(self):
        return f"{self.medic} - {self.pacient}"


class Consultatie(models.Model):
    """Junction table: Pacient <-> Medicament with additional fields"""
    ConsultatieID = models.AutoField(primary_key=True)
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)
    
    Data = models.DateField()
    Diagnostic = models.TextField(blank=True, null=True)
    DozaMedicament = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'consultatie'
        verbose_name_plural = 'Consultatii'
    
    def __str__(self):
        return f"Consultatie {self.ConsultatieID}: {self.pacient} - {self.Data}"
    
    def save(self, *args, **kwargs):
        """Override save to automatically create MedicPacient relationship if it doesn't exist"""
        super().save(*args, **kwargs)  # Save the consultation first
        
        # Create MedicPacient relationship if it doesn't exist
        MedicPacient.objects.get_or_create(
            medic=self.medic,
            pacient=self.pacient
        )
