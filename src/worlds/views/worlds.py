from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from histories.models import History
from histories.serializers import HistorySerializer
from worlds.forms import WorldForm
from worlds.models import World
from accounts.models import UserProfile

# Create your views here.
def index(request, pk, template_name='worlds/index.html', data={}):
    data['creator'] = UserProfile.objects.get(pk=pk, user=request.user)
    return render(request, template_name, data)

def view_world(request, pk, template_name='worlds/world_view.html', data={}):
    data['world'] = World.objects.get(pk=pk, creator=request.user.profile)
    return render(request, template_name, data)

def create_world(request, template_name='worlds/world_form.html', data={}):
    form = WorldForm(request.POST or None)
    if form.is_valid():
        c = form.save(commit=False)
        c.creator = request.user.profile
        c.save()
        return redirect('worlds:view-world', c.id)
    data['form'] = form
    return render(request, template_name, data)

@api_view(['GET', 'POST'])
def world_history(request, pk):
    try:
        world = World.objects.get(pk=pk)
    except World.DoesNotExist:
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
            'world': world.pk,
            'creator': request.user.profile.pk
        }
        serializer = HistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)