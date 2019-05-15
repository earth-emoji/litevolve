import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from histories.models import History
from histories.serializers import HistorySerializer
from histories.models import History
from histories.serializers import HistorySerializer
from universes.models import Universe, Particle
from universes.serializers import ParticleSerializer
from accounts.models import UserProfile

def particle_index(request, slug, template_name='particles/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, creator=request.user.profile)
    return render(request, template_name, data)

def particle_view(request, slug, template_name='particles/edit.html', data={}):
    data['particle'] = Particle.objects.get(slug=slug)
    return render(request, template_name, data)
