from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from communities.models import Society, SocialGroup, Religion
from communities.serializers import SocietySerializer, SocialGroupSerializer
from histories.models import History
from histories.serializers import HistorySerializer
from worlds.models import World, Species, Place
from accounts.models import UserProfile

# Create your views here.
def index(request, pk, template_name='social_groups/index.html', data={}):
    data['creator'] = UserProfile.objects.get(pk=pk, user=request.user)
    return render(request, template_name, data)


@api_view(['GET', 'POST'])
def sg_collection(request):
    if request.method == 'GET':
        social_groups = SocialGroup.objects.filter(creator=request.user.profile)
        serializer = SocialGroupSerializer(social_groups, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = SocialGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def sg_single(request, pk):
    try:
        social_group = SocialGroup.objects.get(pk=pk)
    except SocialGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialGroupSerializer(social_group)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        social_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_type(request, pk):
    try:
        social_group = SocialGroup.objects.get(pk=pk)
    except SocialGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialGroupSerializer(social_group)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'type': request.data.get('type')
        }
        serializer = SocialGroupSerializer(social_group, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_goals(request, pk):
    try:
        social_group = SocialGroup.objects.get(pk=pk)
    except SocialGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialGroupSerializer(social_group)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'goals': request.data.get('goals')
        }
        serializer = SocialGroupSerializer(social_group, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_structure(request, pk):
    try:
        social_group = SocialGroup.objects.get(pk=pk)
    except SocialGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialGroupSerializer(social_group)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'structure': request.data.get('structure')
        }
        serializer = SocialGroupSerializer(social_group, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_cohes(request, pk):
    try:
        social_group = SocialGroup.objects.get(pk=pk)
    except SocialGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialGroupSerializer(social_group)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'cohesiveness': request.data.get('cohesiveness')
        }
        serializer = SocialGroupSerializer(social_group, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_extra(request, pk):
    try:
        social_group = SocialGroup.objects.get(pk=pk)
    except SocialGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialGroupSerializer(social_group)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'extra': request.data.get('extra')
        }
        serializer = SocialGroupSerializer(social_group, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def sgroup_edit(request, pk, template_name='social_groups/edit.html', data={}):
    try:
        social_group = SocialGroup.objects.get(pk=pk)
    except SocialGroup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['sgroup'] = social_group
    return render(request, template_name, data)
