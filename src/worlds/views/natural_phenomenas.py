from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from worlds.models import World, NaturalPhenomena
from worlds.serializers import NaturalPhenomenaSerializer

@api_view(['GET', 'POST'])
def nphenom_collection(request, pk):
    world = World.objects.get(pk=pk)
    if request.method == 'GET':
        natural_phenomenas = NaturalPhenomena.objects.filter(world=world)
        serializer = NaturalPhenomenaSerializer(natural_phenomenas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'), 
            'world': world.pk,
            'creator': request.user.profile.pk
        }
        serializer = NaturalPhenomenaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def nphenom_single(request, pk):
    try:
        natural_phenomena = NaturalPhenomena.objects.get(pk=pk)
    except NaturalPhenomena.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalPhenomenaSerializer(natural_phenomena)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        natural_phenomena.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PATCH'])
def update_desc(request, pk):
    try:
        natural_phenomena = NaturalPhenomena.objects.get(pk=pk)
    except NaturalPhenomena.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NaturalPhenomenaSerializer(natural_phenomena)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'description': request.data.get('description')
        }
        serializer = NaturalPhenomenaSerializer(natural_phenomena, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def nphenom_edit(request, pk, template_name='nphenoms/edit.html', data={}):
    try:
        natural_phenomena = NaturalPhenomena.objects.get(pk=pk)
    except NaturalPhenomena.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['nphenom'] = natural_phenomena
    return render(request, template_name, data)