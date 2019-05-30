from django.urls import include, path

from universes.views import natural_laws

urlpatterns = [
    path('', include(([
        path('natural_laws/creator/<uuid:slug>/',
             natural_laws.rule_index, name='index'),
        path('natural_laws/view/<uuid:slug>/',
             natural_laws.rule_edit, name='edit'),
        path('api/natural_laws/',
             natural_laws.rule_collection, name='collection'),
        path('api/natural_laws/<uuid:slug>/',
             natural_laws.rule_single, name='single'),
        path('api/natural_laws/<uuid:slug>/update-can/',
             natural_laws.update_can, name='update-can'),
        path('api/natural_laws/<uuid:slug>/update-cannot/',
             natural_laws.update_cannot, name='update-cannot'),
        path('api/natural_laws/<uuid:slug>/update-explanation/',
             natural_laws.update_explanation, name='update-explanation'),
    ], 'rules')))
]
