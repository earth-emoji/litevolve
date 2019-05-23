import json
from datetime import datetime, date
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from projects.models import Project, Task
from projects.serializer import ProjectSerializer, TaskSerializer
from universes.models import (NaturalLaw,
                                CelestialBody,
                                NaturalPhenomena,
                                Season,
                                NaturalObject,
                                Species,
                                Place,
                                Particle,
                                Element,
                                Universe)
from utils import calc

def edit(request, slug, template_name='tasks/edit.html', data={}):
    data['task'] = Task.objects.get(slug=slug)
    return render(request, template_name, data)

@api_view(['GET', 'POST'])
def task_collection(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        tasks = Task.objects.filter(project=project)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'day': date.today(),
            'project': project.pk,
            'creator': request.user.profile.pk
        }
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            json_resp = {
                'data': serializer.data,
                'progress': project.progress
            }
            return JsonResponse(json_resp, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def task_single(request, slug):
    try:
        task = Task.objects.get(slug=slug)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def create_ctype(request, slug):
    try:
        task = Task.objects.get(slug=slug)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        if request.POST['ctype'] == 'Universe':
            ctype = Universe.objects.create(name=request.POST['name'], creator=request.user.profile)
        task.content_object = ctype
        task.save()
        data = {
            'slug': ctype.slug,
            'name': ctype.name,
            'url': ctype.url,
        }
        return JsonResponse(data)

@api_view(['GET', 'PATCH'])
def update_complete(request, slug):
    try:
        task = Task.objects.get(slug=slug)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    if request.method == 'PATCH':
        data = {
            'is_complete': request.data.get('is_complete'),
        }
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
