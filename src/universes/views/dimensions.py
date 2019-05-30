import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from universes.models import Universe, Dimension
from universes.serializers import UniverseSerializer, DimensionSerializer
from accounts.models import UserProfile

def dimension_index(request, slug, template_name='dimensions/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, user=request.user)
    return render(request, template_name, data)


def dimension_edit(request, slug, template_name='dimensions/edit.html', data={}):
    try:
        dimension = Dimension.objects.get(slug=slug)
    except Dimension.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['dimension'] = dimension
    return render(request, template_name, data)

@api_view(['GET', 'POST'])
def dimension_collection(request):
    if request.method == 'GET':
        dimensions = Dimension.objects.filter(creator=request.user.profile)
        serializer = DimensionSerializer(dimensions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = DimensionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def dimension_single(request, slug):
    try:
        dimension = Element.objects.get(slug=slug)
    except Dimension.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DimensionSerializer(dimension)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        dimension.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
