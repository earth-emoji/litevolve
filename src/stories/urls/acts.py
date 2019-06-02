from django.urls import include, path

from stories.views import acts

urlpatterns = [
    path('', include(([
        path('acts/view/<uuid:slug>/', acts.act_edit, name='edit'),
        path('api/story/<uuid:slug>/acts/', acts.act_collection, name='collection'),
    ], 'acts'))),
]
