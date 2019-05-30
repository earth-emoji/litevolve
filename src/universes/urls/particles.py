from django.urls import include, path

from universes.views import particles

urlpatterns = [
    path('', include(([
        path('particles/creator/<uuid:slug>/',
             particles.index, name='particle-index'),
        path('particles/view/<uuid:slug>/',
             particles.edit, name='particle-edit'),
        path('api/particles/',
             particles.particle_collection, name='particle-collection'),
        path('api/particles/<uuid:slug>/',
             particles.particle_single, name='particle-single'),
        path('api/particles/<uuid:slug>/update-description/',
             particles.update_description, name='particle-update-description'),
    ], 'particles')))
]
