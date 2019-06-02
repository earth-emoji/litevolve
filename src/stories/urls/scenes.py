from django.urls import include, path

from stories.views import scenes

urlpatterns = [
    path('', include(([
        path('scenes/view/<uuid:slug>/', scenes.scene_edit, name='edit'),
        path('api/chapters/<uuid:slug>/scenes/', scenes.scene_collection, name='collection'),
    ], 'scenes'))),
]
