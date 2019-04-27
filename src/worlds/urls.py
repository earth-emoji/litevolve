from django.urls import path, include

from worlds.views import worlds, rules, celestial_bodies, natural_phenomenas, seasons, natural_objects, species, places

urlpatterns = [
    path('', include(([
        path('worlds/creator/<int:pk>/', worlds.index, name='index'),
        path('worlds/view/<int:pk>/', worlds.view_world, name='view-world'),
        path('worlds/create/', worlds.create_world, name='create-world'),
        path('rules/view/<int:pk>/', rules.rule_edit, name='rule-edit'),
        path('celestial_bodies/view/<int:pk>/', celestial_bodies.cbody_edit, name='cbody-edit'),
        path('natural_phenomenas/view/<int:pk>/', natural_phenomenas.nphenom_edit, name='nphenom-edit'),
        path('seasons/view/<int:pk>/', seasons.season_edit, name='season-edit'),
        path('natural_objects/view/<int:pk>/', natural_objects.nobject_edit, name='nobject-edit'),
        path('species/view/<int:pk>/', species.species_edit, name='species-edit'),
        path('places/view/<int:pk>/', places.place_edit, name='place-edit'),

        path('api/worlds/<int:pk>/histories/', worlds.world_history, name='world-history'),

        path('api/worlds/<int:pk>/rules/', rules.rule_collection, name='rule-collection'),
        path('api/rules/<int:pk>/', rules.rule_single, name='rule-single'),
        path('api/rules/<int:pk>/update-can/', rules.update_can, name='rule-update-can'),
        path('api/rules/<int:pk>/update-cannot/', rules.update_cannot, name='rule-update-cannot'),
        path('api/rules/<int:pk>/update-explanation/', rules.update_explanation, name='rule-update-explanation'),
        
        path('api/worlds/<int:pk>/celestial_bodies/', celestial_bodies.cbody_collection, name='cbody-collection'),
        path('api/celestial_bodies/<int:pk>/', celestial_bodies.cbody_single, name='cbody-single'),
        path('api/celestial_bodies/<int:pk>/update-description/', celestial_bodies.update_desc, name='cbody-update-description'),

        path('api/worlds/<int:pk>/natural_phenomenas/', natural_phenomenas.nphenom_collection, name='nphenom-collection'),
        path('api/natural_phenomenas/<int:pk>/', natural_phenomenas.nphenom_single, name='nphenom-single'),
        path('api/natural_phenomenas/<int:pk>/update-description/', natural_phenomenas.update_desc, name='nphenom-update-description'),

        path('api/worlds/<int:pk>/seasons/', seasons.season_collection, name='season-collection'),
        path('api/seasons/<int:pk>/', seasons.season_single, name='season-single'),
        path('api/seasons/<int:pk>/update-description/', seasons.update_desc, name='season-update-description'),

        path('api/worlds/<int:pk>/natural_objects/', natural_objects.nobject_collection, name='nobject-collection'),
        path('api/natural_objects/<int:pk>/', natural_objects.nobject_single, name='nobject-single'),
        path('api/natural_objects/<int:pk>/update-appearance/', natural_objects.update_appearance, name='nobject-update-appearance'),
        path('api/natural_objects/<int:pk>/update-history/', natural_objects.update_history, name='nobject-update-history'),
        path('api/natural_objects/<int:pk>/update-value/', natural_objects.update_value, name='nobject-update-value'),

        path('api/worlds/<int:pk>/species/', species.species_collection, name='species-collection'),
        path('api/species/<int:pk>/', species.species_single, name='species-single'),
        path('api/species/<int:pk>/update-appearance/', species.update_appearance, name='species-update-appearance'),
        path('api/species/<int:pk>/update-abilities/', species.update_abilities, name='species-update-abilites'),
        path('api/species/<int:pk>/update-intelligence/', species.update_intelligence, name='species-update-intelligence'),
        path('api/species/<int:pk>/update-origins/', species.update_origins, name='species-update-origins'),
        path('api/species/<int:pk>/update-habitat/', species.update_habitat, name='species-update-habitat'),
        path('api/species/<int:pk>/update-ecosystem/', species.update_ecosystem, name='species-update-ecosystem'),
        path('api/species/<int:pk>/update-diet/', species.update_diet, name='species-update-diet'),
        path('api/species/<int:pk>/update-predators/', species.update_predators, name='species-update-predators'),
        path('api/species/<int:pk>/update-defense/', species.update_defense, name='species-update-defense'),
        path('api/species/<int:pk>/update-extra/', species.update_extra, name='species-update-extra'),

        path('api/worlds/<int:pk>/places/', places.place_collection, name='place-collection'),
        path('api/places/<int:pk>/', places.place_single, name='place-single'),
        path('api/places/<int:pk>/update-scenery/', places.update_scenery, name='places-update-scenery'),
        path('api/places/<int:pk>/update-description/', places.update_description, name='places-update-description'),
    ], 'worlds'), namespace='worlds'))
]
 