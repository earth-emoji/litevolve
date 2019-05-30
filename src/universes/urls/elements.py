from django.urls import include, path

from universes.views import elements

urlpatterns = [
    path('', include(([
        path('elements/creator/<uuid:slug>/', elements.element_index, name='index'),
        path('elements/view/<uuid:slug>/', elements.element_edit, name='edit'),
        path('api/elements/',elements.element_collection, name='collection'),
        path('api/elements/<uuid:slug>/', elements.element_single, name='single'),
    ], 'elements')))
]
