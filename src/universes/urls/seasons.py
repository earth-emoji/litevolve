from django.urls import include, path

from universes.views import seasons

urlpatterns = [
    path('', include(([
        path('seasons/creator/<uuid:slug>/',
             seasons.season_index, name='index'),
        path('seasons/view/<uuid:slug>/',
             seasons.season_edit, name='edit'),
        path('api/seasons/',
             seasons.season_collection, name='collection'),
        path('api/seasons/<uuid:slug>/',
             seasons.season_single, name='single'),
        path('api/seasons/<uuid:slug>/update-description/',
             seasons.update_desc, name='update-description'),
    ], 'seasons')))
]
