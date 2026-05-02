from django.db import models
from django.utils import timezone

class Espece(models.Model):
    nom_espece = models.CharField(max_length=100, unique=True, verbose_name="Nom de l'espèce")
    besoins_specifiques = models.TextField(blank=True, verbose_name="Besoins spécifiques")

    def __str__(self):
        return self.nom_espece

class Animal(models.Model):
    STATUT_CHOICES = [
        ('Disponible', 'Disponible'),
        ('En soin', 'En soin'),
        ('Adopté', 'Adopté'),
        ('En famille d\'accueil', 'En famille d\'accueil'),
    ]

    SEXE_CHOICES = [
        ('M', 'Mâle'),
        ('F', 'Femelle'),
    ]

    nom = models.CharField(max_length=100, verbose_name="Nom de l'animal")
    espece = models.ForeignKey(Espece, on_delete=models.CASCADE, related_name='animaux', verbose_name="Espèce")
    race = models.CharField(max_length=100, blank=True, verbose_name="Race")
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES, default='M', verbose_name="Sexe")
    date_naissance_estimee = models.DateField(verbose_name="Date de naissance estimée")
    
    # Santé
    vaccine = models.BooleanField(default=False, verbose_name="Vacciné")
    sterilise = models.BooleanField(default=False, verbose_name="Stérilisé")
    
    # Compatibilités
    compatibilite_chats = models.BooleanField(default=False, verbose_name="Entente Chats")
    compatibilite_chiens = models.BooleanField(default=False, verbose_name="Entente Chiens")
    compatibilite_enfants = models.BooleanField(default=False, verbose_name="Entente Enfants")
    
    # Séjour
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='Disponible', verbose_name="Statut")
    date_arrivee = models.DateField(default=timezone.now, verbose_name="Date d'arrivée")

    class Meta:
        verbose_name_plural = "Animaux"

    def __str__(self):
        return f"{self.nom} ({self.espece})"

class Adoption(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name='adoption')
    nom_adoptant = models.CharField(max_length=255, verbose_name="Nom de l'adoptant")
    date_adoption = models.DateField(default=timezone.now, verbose_name="Date d'adoption")
    frais_participation = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Frais de participation (€)")

    def __str__(self):
        return f"Adoption de {self.animal.nom} par {self.nom_adoptant}"
