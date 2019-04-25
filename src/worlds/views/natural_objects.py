from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from worlds.models import NaturalObject, World
from worlds.serializers import NaturalObjectSerializer

@api_view(['GET', 'POST'])
def nobject_collection(request, pk):
    world = World.objects.get(pk=pk)
    if request.method == 'GET':
        nobjects = NaturalObject.objects.filter(world=world)
        serializer = NaturalObjectSerializer(nobjects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'), 
            'world': world.pk,
            'creator': request.user.profile.pk
        }
        serializer = NaturalObjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def nobject_single(request, pk):
    try:
        nobject = NaturalObject.objects.get(pk=pk)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalObjectSerializer(nobject)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        nobject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PATCH'])
def update_appearance(request, pk):
    try:
        natural_object = NaturalObject.objects.get(pk=pk)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NaturalObjectSerializer(natural_object)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'appearance': request.data.get('appearance')
        }
        serializer = NaturalObjectSerializer(natural_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def update_history(request, pk):
    try:
        natural_object = NaturalObject.objects.get(pk=pk)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NaturalObjectSerializer(natural_object)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'history': request.data.get('history')
        }
        serializer = NaturalObjectSerializer(natural_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def update_value(request, pk):
    try:
        natural_object = NaturalObject.objects.get(pk=pk)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NaturalObjectSerializer(natural_object)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'value': request.data.get('value'),
            'value_description': request.data.get('value_description')
        }
        serializer = NaturalObjectSerializer(natural_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def nobject_edit(request, pk, template_name='nobjects/edit.html', data={}):
    try:
        natural_object = NaturalObject.objects.get(pk=pk)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['nobject'] = natural_object
    return render(request, template_name, data)