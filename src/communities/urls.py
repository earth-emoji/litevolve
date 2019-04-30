from django.urls import path, include

from communities.views import societies, religions, social_groups

urlpatterns = [
    path('', include(([
        path('societies/creator/<int:pk>/',
             societies.index, name='society-index'),
        path('api/societies/', societies.society_collection,
             name='society-collection'),
        path('societies/view/<int:pk>/',
             societies.society_edit, name='society-edit'),
        path('api/societies/<int:pk>/update-type/', societies.update_type,
             name='society-update-type'),
        path('api/societies/<int:pk>/update-gov/', societies.update_gov,
             name='society-update-gov'),
        path('api/societies/<int:pk>/update-leadership/', societies.update_lead,
             name='society-update-leadership'),
        path('api/societies/<int:pk>/update-military/', societies.update_military,
             name='society-update-military'),
        path('api/societies/<int:pk>/update-social-capital/', societies.update_social_capital,
             name='society-update-social-capital'),

         path('religions/creator/<int:pk>/',
              religions.index, name='religion-index'),
         path('api/religions/', religions.religion_collection,
              name='religion-collection'),

         path('social_groups/creator/<int:pk>/',
              social_groups.index, name='social-group-index'),
         path('api/social_groups/', social_groups.sg_collection,
              name='social-group-collection'),
         ], 'communities'), namespace='communities'))
]
