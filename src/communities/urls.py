from django.urls import path, include

from communities.views import societies, religions, social_groups

urlpatterns = [
    path('', include(([
        path('societies/creator/<uuid:slug>/',
             societies.index, name='society-index'),
        path('api/societies/', societies.society_collection,
             name='society-collection'),
        path('societies/view/<uuid:slug>/',
             societies.society_edit, name='society-edit'),
        path('api/societies/<uuid:slug>/update-type/', societies.update_type,
             name='society-update-type'),
        path('api/societies/<uuid:slug>/update-gov/', societies.update_gov,
             name='society-update-gov'),
        path('api/societies/<uuid:slug>/update-leadership/', societies.update_lead,
             name='society-update-leadership'),
        path('api/societies/<uuid:slug>/update-military/', societies.update_military,
             name='society-update-military'),
        path('api/societies/<uuid:slug>/update-social-capital/', societies.update_social_capital,
             name='society-update-social-capital'),
        path('api/societies/<uuid:slug>/update-hierarchy/', societies.update_hierarchy,
             name='society-update-hierarchy'),
        path('api/societies/<uuid:slug>/update-origin/', societies.update_origin,
             name='society-update-origin'),
        path('api/societies/<uuid:slug>/update-economy/', societies.update_economy,
             name='society-update-economy'),
        path('api/societies/<uuid:slug>/update-legal/', societies.update_legal,
             name='society-update-legal'),
        path('api/societies/<uuid:slug>/update-rivals/', societies.update_rivals,
             name='society-update-rivals'),
        path('api/societies/<uuid:slug>/update-extra/', societies.update_extra,
             name='society-update-extra'),

         path('religions/creator/<uuid:slug>/',
              religions.index, name='religion-index'),
         path('api/religions/', religions.religion_collection,
              name='religion-collection'),
         path('religions/view/<uuid:slug>/', religions.religion_edit,
              name='religion-edit'),
         path('api/religions/<uuid:slug>/update-deities/', religions.update_deities,
              name='religion-update-deities'),
         path('api/religions/<uuid:slug>/update-beliefs/', religions.update_beliefs,
              name='religion-update-beliefs'),
         path('api/religions/<uuid:slug>/update-practices/', religions.update_practices,
              name='religion-update-practices'),
         path('api/religions/<uuid:slug>/update-origins/', religions.update_origins,
              name='religion-update-origins'),
         path('api/religions/<uuid:slug>/update-organization/', religions.update_org,
              name='religion-update-org'),
         path('api/religions/<uuid:slug>/update-holy-objects/', religions.update_hobj,
              name='religion-update-hobj'),
         path('api/religions/<uuid:slug>/update-holidays/', religions.update_holidays,
              name='religion-update-holidays'),
         path('api/religions/<uuid:slug>/update-figures/', religions.update_rfigs,
              name='religion-update-figures'),
         path('api/religions/<uuid:slug>/update-extra/', religions.update_extra,
              name='religion-update-extra'),

         path('social_groups/creator/<uuid:slug>/',
              social_groups.index, name='social-group-index'),
         path('api/social_groups/', social_groups.sg_collection,
              name='social-group-collection'),
         path('social_groups/view/<uuid:slug>/', social_groups.sgroup_edit,
              name='sgroup-edit'),
         path('api/social_groups/<uuid:slug>/update-type/', social_groups.update_type,
              name='sgroup-update-type'),
         path('api/social_groups/<uuid:slug>/update-goals/', social_groups.update_goals,
              name='sgroup-update-goals'),
         path('api/religions/<uuid:slug>/update-structure/', social_groups.update_structure,
              name='sgroup-update-structure'),
         path('api/social_groups/<uuid:slug>/update-structure/', social_groups.update_structure,
              name='sgroup-update-structure'),
         path('api/social_groups/<uuid:slug>/update-cohesiveness/', social_groups.update_cohes,
              name='sgroup-update-cohes'),
         path('api/social_groups/<uuid:slug>/update-extra/', social_groups.update_extra,
              name='sgroup-update-extra'),
         ], 'communities'), namespace='communities'))
]
