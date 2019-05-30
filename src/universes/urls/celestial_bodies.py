from django.urls import include, path

from universes.views import celestial_bodies

urlpatterns = [
    path('', include(([
        path('celestial_bodies/creator/<uuid:slug>/',
             celestial_bodies.cbody_index, name='index'),
        path('celestial_bodies/view/<uuid:slug>/',
             celestial_bodies.cbody_edit, name='edit'),
        path('api/celestial_bodies/',
             celestial_bodies.cbody_collection, name='collection'),
        path('api/celestial_bodies/<uuid:slug>/',
             celestial_bodies.cbody_single, name='single'),
        path('api/celestial_bodies/<uuid:slug>/update-description/',
             celestial_bodies.update_desc, name='update-description'),
    ], 'celestial_bodies')))
]
