from django.urls import include, path

from universes.views import dimensions

urlpatterns = [
    path('', include(([
        path('dimensions/creator/<uuid:slug>/', dimensions.dimension_index, name='index'),
        path('dimensions/view/<uuid:slug>/', dimensions.dimension_edit, name='edit'),
        path('api/dimensions/',dimensions.dimension_collection, name='collection'),
        path('api/dimensions/<uuid:slug>/', dimensions.dimension_single, name='single'),
    ], 'dimensions')))
]
