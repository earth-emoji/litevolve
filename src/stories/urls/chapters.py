from django.urls import include, path

from stories.views import chapters

urlpatterns = [
    path('', include(([
        path('chapters/view/<uuid:slug>/', chapters.chapter_edit, name='edit'),
        path('api/acts/<uuid:slug>/chapters/', chapters.chapter_collection, name='collection'),
    ], 'chapters'))),
]
