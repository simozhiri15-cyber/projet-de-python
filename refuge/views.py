from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
from .models import Animal, Espece
from .forms import AnimalSearchForm, AnimalForm

def animal_list(request):
    animaux = Animal.objects.all().order_by('-date_arrivee')
    form = AnimalSearchForm(request.GET)
    
    if form.is_valid():
        if form.cleaned_data.get('nom'):
            animaux = animaux.filter(nom__icontains=form.cleaned_data['nom'])
        if form.cleaned_data.get('espece'):
            animaux = animaux.filter(espece=form.cleaned_data['espece'])
        if form.cleaned_data.get('sexe'):
            animaux = animaux.filter(sexe=form.cleaned_data['sexe'])
        if form.cleaned_data.get('entente_chats'):
            animaux = animaux.filter(compatibilite_chats=True)
        if form.cleaned_data.get('entente_chiens'):
            animaux = animaux.filter(compatibilite_chiens=True)
        if form.cleaned_data.get('entente_enfants'):
            animaux = animaux.filter(compatibilite_enfants=True)
            
        duree = form.cleaned_data.get('duree_sejour')
        today = timezone.now().date()
        if duree == 'recent':
            animaux = animaux.filter(date_arrivee__gte=today - datetime.timedelta(days=30))
        elif duree == 'moyen':
            animaux = animaux.filter(date_arrivee__lt=today - datetime.timedelta(days=30), date_arrivee__gte=today - datetime.timedelta(days=180))
        elif duree == 'long':
            animaux = animaux.filter(date_arrivee__lt=today - datetime.timedelta(days=180))
            
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
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm()
    return render(request, 'refuge/animal_form.html', {'form': form, 'title': 'Ajouter un animal'})

@login_required
def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_detail', pk=animal.pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'refuge/animal_form.html', {'form': form, 'title': f'Modifier {animal.nom}'})
