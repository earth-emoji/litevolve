from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .forms import CharacterForm
from .models import Character
from .serializers import CharacterSerializer
from accounts.models import UserProfile
from photos.models import Album, Photo


# Create your views here.
def creator_characters(request, pk, template_name='characters/index.html', data={}):
    creator = UserProfile.objects.get(pk=pk, user=request.user)
    data['creator'] = creator
    return render(request, template_name, data)


def create_character(request, template_name='characters/character_form.html', data={}):

    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            c = form.save(commit=False)
            c.creator = request.user.profile
            album = Album.objects.create(name=c.name, owner=request.user.profile)
            photo = Photo.objects.create(file=form.cleaned_data['photo'], default=True, album=album)
            c.album = album
            c.save()
            return redirect('characters:my-characters', request.user.profile.id)
    else:
        form = CharacterForm()
    data['form'] = form
    return render(request, template_name, data)


@api_view(['GET', 'POST'])
def character_collection(request):
    if request.method == 'GET':
        characters = Character.objects.filter(creator=request.user.profile)
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = CharacterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def character_single(request, pk):
    try:
        character = Character.objects.get(pk=pk)
    except Character.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
