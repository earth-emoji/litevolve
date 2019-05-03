from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from histories.models import History
from histories.serializers import HistorySerializer
from universes.models import Universe
from universes.serializers import UniverseSerializer
from accounts.models import UserProfile


# Create your views here.
def index(request, slug, template_name='universe/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, user=request.user)
    return render(request, template_name, data)


def view_universe(request, slug, template_name='universes/edit.html', data={}):
    data['universe'] = Universe.objects.get(slug=slug, creator=request.user.profile)
    return render(request, template_name, data)


@api_view(['GET', 'POST'])
def universe_collection(request):
    if request.method == 'GET':
        universes = Universe.objects.filter(creator=request.user.profile)
        serializer = UniverseSerializer(universes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = UniverseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def universe_single(request, slug):
    try:
        universe = Universe.objects.get(slug=slug)
    except Universe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UniverseSerializer(universe)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        universe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def universe_history(request, slug):
    try:
        universe = Universe.objects.get(slug=slug)
    except Universe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        histories = History.objects.all().order_by('-year')
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'year': request.data.get('year'),
            'description': request.data.get('description'),
            'universe': universe.pk,
            'creator': request.user.profile.pk
        }
        serializer = HistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
