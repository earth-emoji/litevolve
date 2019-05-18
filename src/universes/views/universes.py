import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from histories.models import History
from histories.serializers import HistorySerializer
from universes.models import Universe, NaturalLaw, Particle
from universes.serializers import UniverseSerializer, NaturalLawSerializer, ParticleSerializer
from accounts.models import UserProfile


# Create your views here.
def index(request, slug, template_name='universes/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, user=request.user)
    return render(request, template_name, data)


def view_universe(request, slug, template_name='universes/edit.html', data={}):
    try:
        universe = Universe.objects.get(slug=slug)
    except Universe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['laws'] = NaturalLaw.objects.filter(creator=request.user.profile).exclude(universes__id=universe.id)
    data['particles'] = Particle.objects.filter(creator=request.user.profile).exclude(universes__id=universe.id)
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


@api_view(['GET', 'PATCH'])
def update_overview(request, slug):
    try:
        universe = Universe.objects.get(slug=slug)
    except Universe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UniverseSerializer(universe)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'overview': request.data.get('overview')
        }
        serializer = UniverseSerializer(universe, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'POST'])
def universe_law(request, slug):
    try:
        universe = Universe.objects.get(slug=slug)
    except Universe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        rules = NaturalLaw.objects.filter(universes__id=universe.id)
        serializer = NaturalLawSerializer(rules, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        slug = request.POST['natural_law']
        law = NaturalLaw.objects.get(slug=slug)
        universe.natural_laws.add(law)
        data = {
            'slug': law.slug,
            'name': law.name, 
        }
        return JsonResponse(data, safe=False)

@api_view(['GET', 'POST'])
def universe_particle(request, slug):
    try:
        universe = Universe.objects.get(slug=slug)
    except Universe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        particles = Particle.objects.filter(universes__id=universe.id)
        serializer = ParticleSerializer(particles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        slug = request.POST['particle']
        particle = Particle.objects.get(slug=slug)
        universe.particles.add(particle)
        data = {
            'slug': particle.slug,
            'name': particle.name, 
        }
        return JsonResponse(data)
    

    

    