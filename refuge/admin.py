from django.contrib import admin
from .models import Espece, Animal, Adoption

@admin.register(Espece)
class EspeceAdmin(admin.ModelAdmin):
    list_display = ('nom_espece',)

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nom', 'espece', 'sexe', 'statut', 'date_arrivee', 'vaccine', 'sterilise')
    list_filter = ('statut', 'espece', 'sexe', 'vaccine', 'sterilise')
    search_fields = ('nom', 'race')

@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('animal', 'nom_adoptant', 'date_adoption', 'frais_participation')
    search_fields = ('nom_adoptant', 'animal__nom')
