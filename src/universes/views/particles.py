import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from universes.models import Universe, Particle
from universes.serializers import ParticleSerializer
from accounts.models import UserProfile

def index(request, slug, template_name='particles/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug)
    return render(request, template_name, data)

def edit(request, slug, template_name='particles/edit.html', data={}):
    data['particle'] = Particle.objects.get(slug=slug)
    return render(request, template_name, data)

@api_view(['GET', 'POST'])
def particle_collection(request):
    if request.method =='GET':
        particles = Particle.objects.filter(creator=request.user.profile)
        serializer = ParticleSerializer(particles, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'size': request.data.get('size'),
            'creator': request.user.profile.pk
        }
        serializer = ParticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def particle_single(request, slug):
    try:
        particle = Particle.objects.get(slug=slug)
    except Particle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParticleSerializer(particle)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        particle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PATCH'])
def update_description(request, slug):
    try:
        particle = Particle.objects.get(slug=slug)
    except Particle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ParticleSerializer(particle)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'description': request.data.get('description')
        }
        
        serializer = ParticleSerializer(particle, data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
