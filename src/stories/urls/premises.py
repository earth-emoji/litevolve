from django.urls import include, path

from stories.views import premises

urlpatterns = [
    path('', include(([
        # path('api/premises/', premises.story_collection, name='collection'),
        # path('api/premises/<uuid:slug>/', stories.story_single, name='single'),

        path('api/premises/<uuid:slug>/update-synopsis/', premises.update_synopsis, name='update-synopsis'),
        path('api/premises/<uuid:slug>/update-setting/', premises.update_setting, name='update-setting'),
        path('api/premises/<uuid:slug>/update-ending/', premises.update_ending, name='update-ending'),
        path('api/premises/<uuid:slug>/update-beginning/', premises.update_beginning, name='update-beginning'),
    ], 'premises'))),
]
