from django.urls import include, path

from stories.views import stories

urlpatterns = [
    path('', include(([
        path('stories/creator/<uuid:slug>/', stories.story_index, name='index'),
        path('stories/view/<uuid:slug>/', stories.story_edit, name='edit'),

        path('api/stories/', stories.story_collection, name='collection'),
        path('api/stories/<uuid:slug>/', stories.story_single, name='single'),
    ], 'stories'))),
]
