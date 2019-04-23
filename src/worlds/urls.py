from django.urls import path, include

from worlds.views import worlds, rules

urlpatterns = [
    path('', include(([
        path('worlds/creator/<int:pk>/', worlds.index, name='index'),
        path('worlds/view/<int:pk>/', worlds.view_world, name='view-world'),
        path('worlds/create/', worlds.create_world, name='create-world'),
        path('rules/view/<int:pk>/', rules.rule_edit, name='rule-edit'),
        path('api/worlds/<int:pk>/histories/', worlds.world_history, name='world-history'),
        path('api/worlds/<int:pk>/rules/', rules.rule_collection, name='rule-collection'),
        path('api/rules/<int:pk>/', rules.rule_single, name='rule-single'),
        path('api/rules/<int:pk>/update-can/', rules.update_can, name='rule-update-can'),
        path('api/rules/<int:pk>/update-cannot/', rules.update_cannot, name='rule-update-cannot'),
        path('api/rules/<int:pk>/update-explanation/', rules.update_explanation, name='rule-update-explanation'),
    ], 'worlds'), namespace='worlds'))
]
 