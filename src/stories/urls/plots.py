from django.urls import include, path

from stories.views import plots

urlpatterns = [
    path('', include(([
        path('api/plots/<uuid:slug>/update-exposition/', plots.update_exposition, name='update-exposition'),
        path('api/plots/<uuid:slug>/update-conflict/', plots.update_conflict, name='update-conflict'),
        path('api/plots/<uuid:slug>/update-rising_action/', plots.update_ract, name='update-ract'),
        path('api/plots/<uuid:slug>/update-climax/', plots.update_climax, name='update-climax'),
        path('api/plots/<uuid:slug>/update-falling_action/', plots.update_fact, name='update-fact'),
        path('api/plots/<uuid:slug>/update-resolution/', plots.update_reso, name='update-resolution'),
    ], 'plots'))),
]
