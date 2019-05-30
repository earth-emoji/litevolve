from django.urls import include, path

from universes.views import natural_objects

urlpatterns = [
    path('', include(([
        path('natural_objects/creator/<uuid:slug>/',
             natural_objects.nobject_index, name='index'),
        path('natural_objects/view/<uuid:slug>/',
             natural_objects.nobject_edit, name='edit'),
        path('api/natural_objects/',
             natural_objects.nobject_collection, name='collection'),
        path('api/natural_objects/<uuid:slug>/',
             natural_objects.nobject_single, name='single'),
        path('api/natural_objects/<uuid:slug>/update-appearance/',
             natural_objects.update_appearance, name='update-appearance'),
        path('api/natural_objects/<uuid:slug>/update-history/',
             natural_objects.update_history, name='update-history'),
        path('api/natural_objects/<uuid:slug>/update-value/',
             natural_objects.update_value, name='update-value'),
    ], 'natural_objects')))
]
