from django.urls import include, path

from universes.views import species

urlpatterns = [
    path('', include(([
         path('species/creator/<uuid:slug>/',
             species.species_index, name='index'),
        path('species/view/<uuid:slug>/',
             species.species_edit, name='edit'),
        path('api/species/',
             species.species_collection, name='species-collection'),
        path('api/species/<uuid:slug>/',
             species.species_single, name='species-single'),
        path('api/species/<uuid:slug>/update-appearance/',
             species.update_appearance, name='species-update-appearance'),
        path('api/species/<uuid:slug>/update-abilities/',
             species.update_abilities, name='species-update-abilites'),
        path('api/species/<uuid:slug>/update-intelligence/',
             species.update_intelligence, name='species-update-intelligence'),
        path('api/species/<uuid:slug>/update-origins/',
             species.update_origins, name='species-update-origins'),
        path('api/species/<uuid:slug>/update-habitat/',
             species.update_habitat, name='species-update-habitat'),
        path('api/species/<uuid:slug>/update-ecosystem/',
             species.update_ecosystem, name='species-update-ecosystem'),
        path('api/species/<uuid:slug>/update-diet/',
             species.update_diet, name='species-update-diet'),
        path('api/species/<uuid:slug>/update-predators/',
             species.update_predators, name='species-update-predators'),
        path('api/species/<uuid:slug>/update-defense/',
             species.update_defense, name='species-update-defense'),
        path('api/species/<uuid:slug>/update-extra/',
             species.update_extra, name='species-update-extra'),
    ], 'species')))
]
