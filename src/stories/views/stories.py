import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from stories.models import Story
from stories.serializers import StorySerializer

def story_index(request, slug, template_name='stories/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, user=request.user)
    return render(request, template_name, data)

def story_edit(request, slug, template_name='stories/edit.html', data={}):
    try:
        data['story'] = Story.objects.get(slug=slug)
    except Story.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return render(request, template_name, data)

@api_view(['GET', 'POST'])
def story_collection(request):
    if request.method == 'GET':
        stories = Story.objects.filter(author=request.user.profile)
        serializer = StorySerializer(stories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'genre': request.data.get('genre'),
            'author': request.user.profile.pk
        }
        serializer = StorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def story_single(request, slug):
    try:
        story = Story.objects.get(slug=slug)
    except Story.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StorySerializer(story)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
