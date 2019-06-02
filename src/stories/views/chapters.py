import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from stories.models import Story, Act, Chapter
from stories.serializers import ChapterSerializer

def chapter_edit(request, slug, template_name='chapters/edit.html', data={}):
    try:
        data['chapter'] = Chapter.objects.get(slug=slug)
    except Chapter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return render(request, template_name, data)

@api_view(['GET', 'POST'])
def chapter_collection(request, slug):
    try:
        act = Act.objects.get(slug=slug)
    except Act.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        chapters = Chapter.objects.filter(act=act, author=request.user.profile).order_by('-chap_number')
        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'chap_number': request.data.get('chap_number'),
            'act': act.pk,
            'author': request.user.profile.pk
        }
        serializer = ChapterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'DELETE'])
# def story_single(request, slug):
#     try:
#         story = Story.objects.get(slug=slug)
#     except Story.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StorySerializer(story)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         story.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
