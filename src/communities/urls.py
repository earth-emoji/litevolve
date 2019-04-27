from django.urls import path, include

from communities.views import societies, religions, social_groups

urlpatterns = [
    path('', include(([
        path('societies/creator/<int:pk>/', societies.index, name='society-index'),
        path('api/societies/', societies.society_collection, name='society-collection'),

        path('religions/creator/<int:pk>/', religions.index, name='religion-index'),
        path('api/religions/', religions.religion_collection, name='religion-collection'),

        path('social_groups/creator/<int:pk>/', social_groups.index, name='social-group-index'),
        path('api/social_groups/', social_groups.sg_collection, name='social-group-collection'),
    ], 'communities'), namespace='communities'))
]
 