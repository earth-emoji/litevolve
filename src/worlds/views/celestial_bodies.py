from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from worlds.models import World, CelestialBody
from worlds.serializers import CelestialBodySerializer

@api_view(['GET', 'POST'])
def cbody_collection(request, pk):
    world = World.objects.get(pk=pk)
    if request.method == 'GET':
        celestial_bodies = CelestialBody.objects.filter(world=world)
        serializer = CelestialBodySerializer(celestial_bodies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'), 
            'world': world.pk,
            'creator': request.user.profile.pk
        }
        serializer = CelestialBodySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def cbody_single(request, pk):
    try:
        celestial_body = CelestialBody.objects.get(pk=pk)
    except CelestialBody.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CelestialBodySerializer(celestial_body)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        celestial_body.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PATCH'])
def update_desc(request, pk):
    try:
        celestial_body = CelestialBody.objects.get(pk=pk)
    except CelestialBody.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CelestialBodySerializer(celestial_body)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'description': request.data.get('description')
        }
        serializer = CelestialBodySerializer(celestial_body, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def cbody_edit(request, pk, template_name='cbodies/edit.html', data={}):
    try:
        celestial_body = CelestialBody.objects.get(pk=pk)
    except CelestialBody.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['cbody'] = celestial_body
    return render(request, template_name, data)