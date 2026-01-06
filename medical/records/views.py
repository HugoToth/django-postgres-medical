from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from .models import Medic, Pacient, Medicament, MedicPacient, Consultatie
from .forms import MedicForm, PacientForm, MedicamentForm, ConsultatieForm

# Helper function to check if user is admin
def is_admin(user):
    return user.is_superuser

# ==================== MEDIC VIEWS ====================

@login_required
def medic_list(request):
    medici = Medic.objects.all()
    return render(request, 'medic_list.html', {'medici': medici})

@login_required
def medic_create(request):
    if request.method == 'POST':
        form = MedicForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medic adăugat cu succes!')
            return redirect('records:medic_list')
    else:
        form = MedicForm()
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Adăugare',
        'entity_name': 'Medic',
        'cancel_url': reverse('records:medic_list')
    })

@login_required
def medic_update(request, pk):
    medic = get_object_or_404(Medic, pk=pk)
    if request.method == 'POST':
        form = MedicForm(request.POST, instance=medic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medic modificat cu succes!')
            return redirect('records:medic_list')
    else:
        form = MedicForm(instance=medic)
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Modificare',
        'entity_name': 'Medic',
        'cancel_url': reverse('records:medic_list')
    })

@login_required
@user_passes_test(is_admin)
def medic_delete(request, pk):
    medic = get_object_or_404(Medic, pk=pk)
    if request.method == 'POST':
        medic.delete()
        messages.success(request, 'Medic șters cu succes!')
        return redirect('records:medic_list')
    return render(request, 'confirm_delete.html', {
        'object': medic,
        'cancel_url': reverse('records:medic_list')
    })

# ==================== PACIENT VIEWS ====================

@login_required
def pacient_list(request):
    pacienti = Pacient.objects.all()
    return render(request, 'pacient_list.html', {'pacienti': pacienti})

@login_required
def pacient_create(request):
    if request.method == 'POST':
        form = PacientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pacient adăugat cu succes!')
            return redirect('records:pacient_list')
    else:
        form = PacientForm()
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Adăugare',
        'entity_name': 'Pacient',
        'cancel_url': reverse('records:pacient_list')
    })

@login_required
def pacient_update(request, pk):
    pacient = get_object_or_404(Pacient, pk=pk)
    if request.method == 'POST':
        form = PacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pacient modificat cu succes!')
            return redirect('records:pacient_list')
    else:
        form = PacientForm(instance=pacient)
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Modificare',
        'entity_name': 'Pacient',
        'cancel_url': reverse('records:pacient_list')
    })

@login_required
@user_passes_test(is_admin)
def pacient_delete(request, pk):
    pacient = get_object_or_404(Pacient, pk=pk)
    if request.method == 'POST':
        pacient.delete()
        messages.success(request, 'Pacient șters cu succes!')
        return redirect('records:pacient_list')
    return render(request, 'confirm_delete.html', {
        'object': pacient,
        'cancel_url': reverse('records:pacient_list')
    })

# ==================== MEDICAMENT VIEWS ====================

@login_required
def medicament_list(request):
    medicamente = Medicament.objects.all()
    return render(request, 'medicament_list.html', {'medicamente': medicamente})

@login_required
def medicament_create(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicament adăugat cu succes!')
            return redirect('records:medicament_list')
    else:
        form = MedicamentForm()
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Adăugare',
        'entity_name': 'Medicament',
        'cancel_url': reverse('records:medicament_list')
    })

@login_required
def medicament_update(request, pk):
    medicament = get_object_or_404(Medicament, pk=pk)
    if request.method == 'POST':
        form = MedicamentForm(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicament modificat cu succes!')
            return redirect('records:medicament_list')
    else:
        form = MedicamentForm(instance=medicament)
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Modificare',
        'entity_name': 'Medicament',
        'cancel_url': reverse('records:medicament_list')
    })

@login_required
@user_passes_test(is_admin)
def medicament_delete(request, pk):
    medicament = get_object_or_404(Medicament, pk=pk)
    if request.method == 'POST':
        medicament.delete()
        messages.success(request, 'Medicament șters cu succes!')
        return redirect('records:medicament_list')
    return render(request, 'confirm_delete.html', {
        'object': medicament,
        'cancel_url': reverse('records:medicament_list')
    })

# ==================== CONSULTATIE VIEWS ====================

@login_required
def consultatie_list(request):
    consultatii = Consultatie.objects.select_related('pacient', 'medic', 'medicament').all()
    return render(request, 'consultatie_list.html', {'consultatii': consultatii})

@login_required
def consultatie_create(request):
    if request.method == 'POST':
        form = ConsultatieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consultație adăugată cu succes!')
            return redirect('records:consultatie_list')
    else:
        form = ConsultatieForm()
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Adăugare',
        'entity_name': 'Consultație',
        'cancel_url': reverse('records:consultatie_list')
    })

@login_required
def consultatie_update(request, pk):
    consultatie = get_object_or_404(Consultatie, pk=pk)
    if request.method == 'POST':
        form = ConsultatieForm(request.POST, instance=consultatie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consultație modificată cu succes!')
            return redirect('records:consultatie_list')
    else:
        form = ConsultatieForm(instance=consultatie)
    return render(request, 'generic_form.html', {
        'form': form,
        'action': 'Modificare',
        'entity_name': 'Consultație',
        'cancel_url': reverse('records:consultatie_list')
    })

@login_required
@user_passes_test(is_admin)
def consultatie_delete(request, pk):
    consultatie = get_object_or_404(Consultatie, pk=pk)
    if request.method == 'POST':
        consultatie.delete()
        messages.success(request, 'Consultație ștearsă cu succes!')
        return redirect('records:consultatie_list')
    return render(request, 'confirm_delete.html', {
        'object': consultatie,
        'cancel_url': reverse('records:consultatie_list')
    })

# ==================== MEDIC-PACIENT VIEWS ====================

@login_required
def medicpacient_list(request):
    relations = MedicPacient.objects.select_related('medic', 'pacient').all()
    
    # Add consultation count for each relation
    for relation in relations:
        relation.consultation_count = Consultatie.objects.filter(
            medic=relation.medic,
            pacient=relation.pacient
        ).count()
    
    return render(request, 'medicpacient_list.html', {'relations': relations})