from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from universes.models import Species
from universes.serializers import SpeciesSerializer


@api_view(['GET', 'POST'])
def species_collection(request):
    if request.method == 'GET':
        species = Species.objects.filter(creator=request.user.profile)
        serializer = SpeciesSerializer(species, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = SpeciesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def species_single(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        species.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_appearance(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'appearance': request.data.get('appearance')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_abilities(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'unique_abilities': request.data.get('unique_abilities')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_intelligence(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'intelligence': request.data.get('intelligence')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_origins(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'origins': request.data.get('origins')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_habitat(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'habitat': request.data.get('habitat')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_ecosystem(request, slug):
    try:
        species = Species.objects.get(pk=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'ecosystem': request.data.get('ecosystem')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_diet(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'diet': request.data.get('diet')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_predators(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'predators': request.data.get('predators')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_defense(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'defense': request.data.get('defense')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_extra(request, slug):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpeciesSerializer(species)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'extra': request.data.get('extra')
        }
        serializer = SpeciesSerializer(species, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def species_edit(request, slug, template_name='species/edit.html', data={}):
    try:
        species = Species.objects.get(slug=slug)
    except Species.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['species'] = species
    return render(request, template_name, data)
