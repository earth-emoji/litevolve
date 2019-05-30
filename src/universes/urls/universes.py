from django.urls import include, path

from universes.views import universes

urlpatterns = [
    path('', include(([
        path('universes/creator/<uuid:slug>/', universes.index, name='index'),
        path('universes/view/<uuid:slug>/',
             universes.edit, name='edit'),
        path('api/universes/<uuid:slug>/histories/',
             universes.universe_history, name='universe-history'),
        path('api/universes/',
             universes.universe_collection, name='universe-collection'),
        path('api/universes/<uuid:slug>/',
             universes.universe_single, name='universe-single'),
        path('api/universes/<uuid:slug>/update-overview/',
             universes.update_overview, name='universe-update-overview'),
        path('api/universes/<uuid:slug>/natural_laws/',
             universes.universe_law, name='universe-law'),
        path('api/universes/<uuid:slug>/particles/',
             universes.universe_particle, name='universe-particle'),
    ], 'universes')))
]
