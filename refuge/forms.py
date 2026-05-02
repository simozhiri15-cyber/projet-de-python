from django import forms
from .models import Animal, Espece

class AnimalSearchForm(forms.Form):
    nom = forms.CharField(required=False, label='Nom', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rechercher par nom...'}))
    espece = forms.ModelChoiceField(queryset=Espece.objects.all(), required=False, empty_label="Toutes les espèces", widget=forms.Select(attrs={'class': 'form-select'}))
    sexe = forms.ChoiceField(choices=[('', 'Tous')] + Animal.SEXE_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    
    # Compatibilités
    entente_chats = forms.BooleanField(required=False, label="Ok Chats", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    entente_chiens = forms.BooleanField(required=False, label="Ok Chiens", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    entente_enfants = forms.BooleanField(required=False, label="Ok Enfants", widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    # Durée de séjour
    DUREE_CHOICES = [
        ('', 'Peu importe'),
        ('recent', 'Moins d\'un mois'),
        ('moyen', '1 à 6 mois'),
        ('long', 'Plus de 6 mois'),
    ]
    duree_sejour = forms.ChoiceField(choices=DUREE_CHOICES, required=False, label="Durée de séjour", widget=forms.Select(attrs={'class': 'form-select'}))


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'espece': forms.Select(attrs={'class': 'form-select'}),
            'race': forms.TextInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'date_naissance_estimee': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'vaccine': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sterilise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'compatibilite_chats': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'compatibilite_chiens': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'compatibilite_enfants': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'date_arrivee': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
