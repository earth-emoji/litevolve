from django.urls import path, include

from projects.views import projects, tasks

urlpatterns = [
    path('', include(([
        path('projects/creator/<uuid:slug>/', projects.index, name='index'),
        path('projects/view/<uuid:slug>/',
             projects.edit, name='view'),
        path('api/projects/',
             projects.project_collection, name='project-collection'),
        path('api/projects/<uuid:slug>/',
             projects.project_single, name='project-single'),
        
        path('tasks/view/<uuid:slug>/',
             tasks.edit, name='task-view'),
        path('api/projects/<uuid:slug>/tasks/',
             tasks.task_collection, name='task-collection'),
        path('api/tasks/<uuid:slug>/content_type/', tasks.create_ctype, name="task-ctype"),
        path('api/tasks/<uuid:slug>/update-complete/', tasks.update_complete, name="task-complete")
    ], 'projects'), namespace='projects'))
]
