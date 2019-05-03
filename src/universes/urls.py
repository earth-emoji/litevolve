from django.urls import path, include

from universes.views import (universes,
                             natural_laws,
                             celestial_bodies,
                             natural_phenomenas,
                             seasons,
                             natural_objects,
                             species,
                             places)

urlpatterns = [
    path('', include(([
        # path('worlds/creator/<uuid:slug>/', worlds.index, name='index'),
        path('universes/creator/<uuid:slug>/', universes.index, name='index'),
        path('universes/view/<uuid:slug>/',
             universes.view_universe, name='view-world'),
        path('natural_laws/view/<uuid:slug>/',
             natural_laws.rule_edit, name='rule-edit'),
        path('celestial_bodies/view/<uuid:slug>/',
             celestial_bodies.cbody_edit, name='cbody-edit'),
        path('natural_phenomenas/view/<uuid:slug>/',
             natural_phenomenas.nphenom_edit, name='nphenom-edit'),
        path('seasons/view/<uuid:slug>/',
             seasons.season_edit, name='season-edit'),
        path('natural_objects/view/<uuid:slug>/',
             natural_objects.nobject_edit, name='nobject-edit'),
        path('species/view/<uuid:slug>/',
             species.species_edit, name='species-edit'),
        path('places/view/<uuid:slug>/', places.place_edit, name='place-edit'),

        path('api/universes/<uuid:slug>/histories/',
             universes.universe_history, name='universe-history'),

        path('api/natural_laws/',
             natural_laws.rule_collection, name='rule-collection'),
        path('api/natural_laws/<uuid:slug>/',
             natural_laws.rule_single, name='rule-single'),
        path('api/natural_laws/<uuid:slug>/update-can/',
             natural_laws.update_can, name='rule-update-can'),
        path('api/natural_laws/<uuid:slug>/update-cannot/',
             natural_laws.update_cannot, name='rule-update-cannot'),
        path('api/natural_laws/<uuid:slug>/update-explanation/',
             natural_laws.update_explanation, name='rule-update-explanation'),

        path('api/celestial_bodies/',
             celestial_bodies.cbody_collection, name='cbody-collection'),
        path('api/celestial_bodies/<uuid:slug>/',
             celestial_bodies.cbody_single, name='cbody-single'),
        path('api/celestial_bodies/<uuid:slug>/update-description/',
             celestial_bodies.update_desc, name='cbody-update-description'),

        path('api/natural_phenomenas/',
             natural_phenomenas.nphenom_collection, name='nphenom-collection'),
        path('api/natural_phenomenas/<uuid:slug>/',
             natural_phenomenas.nphenom_single, name='nphenom-single'),
        path('api/natural_phenomenas/<uuid:slug>/update-description/',
             natural_phenomenas.update_desc, name='nphenom-update-description'),

        path('api/seasons/',
             seasons.season_collection, name='season-collection'),
        path('api/seasons/<uuid:slug>/',
             seasons.season_single, name='season-single'),
        path('api/seasons/<uuid:slug>/update-description/',
             seasons.update_desc, name='season-update-description'),

        path('api/natural_objects/',
             natural_objects.nobject_collection, name='nobject-collection'),
        path('api/natural_objects/<uuid:slug>/',
             natural_objects.nobject_single, name='nobject-single'),
        path('api/natural_objects/<uuid:slug>/update-appearance/',
             natural_objects.update_appearance, name='nobject-update-appearance'),
        path('api/natural_objects/<uuid:slug>/update-history/',
             natural_objects.update_history, name='nobject-update-history'),
        path('api/natural_objects/<uuid:slug>/update-value/',
             natural_objects.update_value, name='nobject-update-value'),

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

        path('api/places/',
             places.place_collection, name='place-collection'),
        path('api/places/<uuid:slug>/', places.place_single, name='place-single'),
        path('api/places/<uuid:slug>/update-scenery/',
             places.update_scenery, name='places-update-scenery'),
        path('api/places/<uuid:slug>/update-description/',
             places.update_description, name='places-update-description'),
    ], 'universes'), namespace='universes'))
]
