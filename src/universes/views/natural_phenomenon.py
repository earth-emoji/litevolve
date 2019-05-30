from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from universes.models import NaturalPhenomena
from universes.serializers import NaturalPhenomenaSerializer


def nphenom_index(request, slug, template_name='nphenoms/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, user=request.user)
    return render(request, template_name, data)


def nphenom_edit(request, slug, template_name='nphenoms/edit.html', data={}):
    try:
        natural_phenomena = NaturalPhenomena.objects.get(slug=slug)
    except NaturalPhenomena.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['nphenom'] = natural_phenomena
    return render(request, template_name, data)


@api_view(['GET', 'POST'])
def nphenom_collection(request):
    if request.method == 'GET':
        natural_phenomenon = NaturalPhenomena.objects.filter(
            creator=request.user.profile)
        serializer = NaturalPhenomenaSerializer(natural_phenomenon, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = NaturalPhenomenaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def nphenom_single(request, slug):
    try:
        natural_phenomena = NaturalPhenomena.objects.get(slug=slug)
    except NaturalPhenomena.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalPhenomenaSerializer(natural_phenomena)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        natural_phenomena.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_desc(request, slug):
    try:
        natural_phenomena = NaturalPhenomena.objects.get(slug=slug)
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

