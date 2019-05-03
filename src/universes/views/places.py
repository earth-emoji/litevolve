from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from universes.models import Place
from universes.serializers import PlaceSerializer


@api_view(['GET', 'POST'])
def place_collection(request):
    if request.method == 'GET':
        places = Place.objects.filter(creator=request.user.profile)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = PlaceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def place_single(request, slug):
    try:
        place = Place.objects.get(slug=slug)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_scenery(request, slug):
    try:
        place = Place.objects.get(slug=slug)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'scenery': request.data.get('scenery')
        }
        serializer = PlaceSerializer(place, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_description(request, slug):
    try:
        place = Place.objects.get(pk=slug)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaceSerializer(place)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'description': request.data.get('description')
        }
        serializer = PlaceSerializer(place, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def place_edit(request, slug, template_name='places/edit.html', data={}):
    try:
        place = Place.objects.get(slug=slug)
    except Place.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['place'] = place
    return render(request, template_name, data)
