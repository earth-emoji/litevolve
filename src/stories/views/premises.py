import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from stories.models import Story, Premise
from stories.serializers import PremiseSerializer


@api_view(['GET', 'PATCH'])
def update_synopsis(request, slug):
    try:
        premise = Premise.objects.get(slug=slug)
    except Premise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PremiseSerializer(premise)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'synopsis': request.data.get('synopsis')
        }
        serializer = PremiseSerializer(premise, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_setting(request, slug):
    try:
        premise = Premise.objects.get(slug=slug)
    except Premise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PremiseSerializer(premise)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'setting': request.data.get('setting')
        }
        serializer = PremiseSerializer(premise, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_setting(request, slug):
    try:
        premise = Premise.objects.get(slug=slug)
    except Premise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PremiseSerializer(premise)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'setting': request.data.get('setting')
        }
        serializer = PremiseSerializer(premise, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_ending(request, slug):
    try:
        premise = Premise.objects.get(slug=slug)
    except Premise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PremiseSerializer(premise)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'ending': request.data.get('ending')
        }
        serializer = PremiseSerializer(premise, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_beginning(request, slug):
    try:
        premise = Premise.objects.get(slug=slug)
    except Premise.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PremiseSerializer(premise)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'beginning': request.data.get('beginning')
        }
        serializer = PremiseSerializer(premise, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
