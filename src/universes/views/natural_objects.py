from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from universes.models import NaturalObject
from universes.serializers import NaturalObjectSerializer


def nobject_index(request, slug, template_name='nobjects/index.html', data={}):
    data['creator'] = UserProfile.objects.get(slug=slug, user=request.user)
    return render(request, template_name, data)


def nobject_edit(request, slug, template_name='nobjects/edit.html', data={}):
    try:
        natural_object = NaturalObject.objects.get(slug=slug)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['nobject'] = natural_object
    return render(request, template_name, data)


@api_view(['GET', 'POST'])
def nobject_collection(request):
    if request.method == 'GET':
        nobjects = NaturalObject.objects.filter(creator=request.user.profile)
        serializer = NaturalObjectSerializer(nobjects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = NaturalObjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def nobject_single(request, slug):
    try:
        nobject = NaturalObject.objects.get(slug=slug)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalObjectSerializer(nobject)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        nobject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_appearance(request, slug):
    try:
        natural_object = NaturalObject.objects.get(slug=slug)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalObjectSerializer(natural_object)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'appearance': request.data.get('appearance')
        }
        serializer = NaturalObjectSerializer(natural_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_history(request, slug):
    try:
        natural_object = NaturalObject.objects.get(slug=slug)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalObjectSerializer(natural_object)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'history': request.data.get('history')
        }
        serializer = NaturalObjectSerializer(natural_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_value(request, slug):
    try:
        natural_object = NaturalObject.objects.get(slug=slug)
    except NaturalObject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalObjectSerializer(natural_object)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'value': request.data.get('value'),
            'value_description': request.data.get('value_description')
        }
        serializer = NaturalObjectSerializer(natural_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

