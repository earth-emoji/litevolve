from django.urls import path, include

from worlds.views import worlds, rules, celestial_bodies, natural_phenomenas

urlpatterns = [
    path('', include(([
        path('worlds/creator/<int:pk>/', worlds.index, name='index'),
        path('worlds/view/<int:pk>/', worlds.view_world, name='view-world'),
        path('worlds/create/', worlds.create_world, name='create-world'),
        path('rules/view/<int:pk>/', rules.rule_edit, name='rule-edit'),
        path('celestial_bodies/view/<int:pk>/', celestial_bodies.cbody_edit, name='cbody-edit'),
        path('natural_phenomenas/view/<int:pk>/', natural_phenomenas.nphenom_edit, name='nphenom-edit'),

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
    ], 'worlds'), namespace='worlds'))
]
 