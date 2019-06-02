from django.urls import path, include

urlpatterns = [
    path('', include('stories.urls.stories')),
    path('', include('stories.urls.premises')),
    path('', include('stories.urls.plots')),
    path('', include('stories.urls.acts')),
    path('', include('stories.urls.chapters')),
    path('', include('stories.urls.scenes')),
]
