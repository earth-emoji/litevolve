from django.urls import path, include

urlpatterns = [
    path('', include('universes.urls.universes')),
    path('', include('universes.urls.dimensions')),
    path('', include('universes.urls.natural_laws')),
    path('', include('universes.urls.particles')),
    path('', include('universes.urls.elements')),
    path('', include('universes.urls.celestial_bodies')),
    path('', include('universes.urls.natural_phenomenon')),
    path('', include('universes.urls.seasons')),
    path('', include('universes.urls.places')),
    path('', include('universes.urls.natural_objects')),
    path('', include('universes.urls.species')),
]
