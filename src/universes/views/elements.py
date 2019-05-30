import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from universes.models import Universe, Element
from universes.serializers import UniverseSerializer, ElementSerializer
from accounts.models import UserProfile

def element_index(request, slug, template_name='elements/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, user=request.user)
    return render(request, template_name, data)


def element_edit(request, slug, template_name='elements/edit.html', data={}):
    try:
        element = Element.objects.get(slug=slug)
    except Element.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['element'] = element
    return render(request, template_name, data)

@api_view(['GET', 'POST'])
def element_collection(request):
    if request.method == 'GET':
        elements = Element.objects.filter(creator=request.user.profile)
        serializer = ElementSerializer(elements, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = ElementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def element_single(request, slug):
    try:
        element = Element.objects.get(slug=slug)
    except Element.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ElementSerializer(element)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        element.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
