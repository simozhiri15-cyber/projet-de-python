from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Animal, Espece
from .forms import AnimalSearchForm, AnimalForm

def animal_list(request):
    animaux_list = Animal.objects.all().order_by('-date_arrivee')
    form = AnimalSearchForm(request.GET)
    
    if form.is_valid():
        if form.cleaned_data.get('nom'):
            animaux_list = animaux_list.filter(nom__icontains=form.cleaned_data['nom'])
        if form.cleaned_data.get('espece'):
            animaux_list = animaux_list.filter(espece=form.cleaned_data['espece'])
        if form.cleaned_data.get('sexe'):
            animaux_list = animaux_list.filter(sexe=form.cleaned_data['sexe'])
        if form.cleaned_data.get('entente_chats'):
            animaux_list = animaux_list.filter(compatibilite_chats=True)
        if form.cleaned_data.get('entente_chiens'):
            animaux_list = animaux_list.filter(compatibilite_chiens=True)
        if form.cleaned_data.get('entente_enfants'):
            animaux_list = animaux_list.filter(compatibilite_enfants=True)
            
        duree = form.cleaned_data.get('duree_sejour')
        today = timezone.now().date()
        if duree == 'recent':
            animaux_list = animaux_list.filter(date_arrivee__gte=today - datetime.timedelta(days=30))
        elif duree == 'moyen':
            animaux_list = animaux_list.filter(date_arrivee__lt=today - datetime.timedelta(days=30), date_arrivee__gte=today - datetime.timedelta(days=180))
        elif duree == 'long':
            animaux_list = animaux_list.filter(date_arrivee__lt=today - datetime.timedelta(days=180))
            
    # Pagination
    paginator = Paginator(animaux_list, 6) # 6 animaux par page
    page_number = request.GET.get('page')
    animaux = paginator.get_page(page_number)
            
    context = {
        'animaux': animaux,
        'form': form,
    }
    return render(request, 'refuge/animal_list.html', context)

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'refuge/animal_detail.html', {'animal': animal})

@login_required
def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save()
            messages.success(request, f"La fiche de {animal.nom} a été créée avec succès.")
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm()
    return render(request, 'refuge/animal_form.html', {'form': form, 'title': 'NOUVEAU PENSIONNAIRE'})

@login_required
def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, f"Les données de {animal.nom} ont été mises à jour.")
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'refuge/animal_form.html', {'form': form, 'title': f'EDITION : {animal.nom}'})

@login_required
def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        nom = animal.nom
        animal.delete()
        messages.success(request, f"La fiche de {nom} a été supprimée.")
        return redirect('animal_list')
    return render(request, 'refuge/animal_confirm_delete.html', {'animal': animal})

@login_required
def dashboard(request):
    total_animaux = Animal.objects.count()
    disponibles = Animal.objects.filter(statut='Disponible').count()
    adoptes = Animal.objects.filter(statut='Adopté').count()
    en_soin = Animal.objects.filter(statut='En soin').count()
    famille = Animal.objects.filter(statut="En famille d'accueil").count()
    
    chiens = Animal.objects.filter(espece__nom_espece='Chien').count()
    chats = Animal.objects.filter(espece__nom_espece='Chat').count()
    nacs = Animal.objects.filter(espece__nom_espece='NAC').count()
    
    recent_animaux = Animal.objects.all().order_by('-date_arrivee')[:5]
    
    context = {
        'total_animaux': total_animaux,
        'disponibles': disponibles,
        'adoptes': adoptes,
        'en_soin': en_soin,
        'famille': famille,
        'chiens': chiens,
        'chats': chats,
        'nacs': nacs,
        'recent_animaux': recent_animaux,
    }
    return render(request, 'refuge/dashboard.html', context)
