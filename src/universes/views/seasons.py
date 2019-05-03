from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from universes.models import Season
from universes.serializers import SeasonSerializer


@api_view(['GET', 'POST'])
def season_collection(request):
    if request.method == 'GET':
        seasons = Season.objects.filter(creator=request.user.profile)
        serializer = SeasonSerializer(seasons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'span': request.data.get('span'),
            'creator': request.user.profile.pk
        }
        serializer = SeasonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def season_single(request, slug):
    try:
        season = Season.objects.get(slug=slug)
    except Season.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SeasonSerializer(season)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        season.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_desc(request, slug):
    try:
        season = Season.objects.get(slug=slug)
    except Season.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SeasonSerializer(season)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'description': request.data.get('description')
        }
        serializer = SeasonSerializer(season, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def season_edit(request, slug, template_name='seasons/edit.html', data={}):
    try:
        season = Season.objects.get(slug=slug)
    except Season.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['season'] = season
    return render(request, template_name, data)
