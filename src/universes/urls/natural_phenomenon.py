from django.urls import include, path

from universes.views import natural_phenomenon

urlpatterns = [
    path('', include(([
         path('natural_phenomenon/creator/<uuid:slug>/',
             natural_phenomenon.nphenom_index, name='index'),
        path('natural_phenomenon/view/<uuid:slug>/',
             natural_phenomenon.nphenom_edit, name='edit'),
        path('api/natural_phenomenon/',
             natural_phenomenon.nphenom_collection, name='collection'),
        path('api/natural_phenomenon/<uuid:slug>/',
             natural_phenomenon.nphenom_single, name='single'),
        path('api/natural_phenomenon/<uuid:slug>/update-description/',
             natural_phenomenon.update_desc, name='update-description'),
    ], 'natural_phenomenon')))
]
