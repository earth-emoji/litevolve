from django.urls import include, path

from universes.views import places

urlpatterns = [
    path('', include(([
        path('places/creator/<uuid:slug>/', places.place_index, name='index'),
        path('places/view/<uuid:slug>/', places.place_edit, name='edit'),
        path('api/places/',
             places.place_collection, name='collection'),
        path('api/places/<uuid:slug>/', places.place_single, name='single'),
        path('api/places/<uuid:slug>/update-scenery/',
             places.update_scenery, name='update-scenery'),
        path('api/places/<uuid:slug>/update-description/',
             places.update_description, name='update-description'),
    ], 'places')))
]
