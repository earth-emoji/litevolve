import simplejson as json
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from accounts.models import UserProfile
from stories.models import Story, Plot
from stories.serializers import PlotSerializer


@api_view(['GET', 'PATCH'])
def update_exposition(request, slug):
    try:
        plot = Plot.objects.get(slug=slug)
    except Plot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlotSerializer(plot)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'exposition': request.data.get('exposition')
        }
        serializer = PlotSerializer(plot, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_conflict(request, slug):
    try:
        plot = Plot.objects.get(slug=slug)
    except Plot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlotSerializer(plot)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'conflict': request.data.get('conflict')
        }
        serializer = PlotSerializer(plot, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_ract(request, slug):
    try:
        plot = Plot.objects.get(slug=slug)
    except Plot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlotSerializer(plot)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'rising_action': request.data.get('rising_action')
        }
        serializer = PlotSerializer(plot, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_climax(request, slug):
    try:
        plot = Plot.objects.get(slug=slug)
    except Plot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlotSerializer(plot)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'climax': request.data.get('climax')
        }
        serializer = PlotSerializer(plot, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_fact(request, slug):
    try:
        plot = Plot.objects.get(slug=slug)
    except Plot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlotSerializer(plot)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'falling_action': request.data.get('falling_action')
        }
        serializer = PlotSerializer(plot, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_reso(request, slug):
    try:
        plot = Plot.objects.get(slug=slug)
    except Plot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlotSerializer(plot)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'resolution': request.data.get('resolution')
        }
        serializer = PlotSerializer(plot, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
