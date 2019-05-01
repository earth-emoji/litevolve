from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from communities.models import Society, SocialGroup, Religion
from communities.serializers import SocietySerializer, ReligionSerializer
from histories.models import History
from histories.serializers import HistorySerializer
from worlds.models import World, Species, Place
from accounts.models import UserProfile


# Create your views here.
def index(request, pk, template_name='religions/index.html', data={}):
    data['creator'] = UserProfile.objects.get(pk=pk, user=request.user)
    return render(request, template_name, data)


@api_view(['GET', 'POST'])
def religion_collection(request):
    if request.method == 'GET':
        religions = Religion.objects.filter(creator=request.user.profile)
        serializer = ReligionSerializer(religions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = ReligionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def religion_single(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        religion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_deities(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'deities': request.data.get('deities')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_beliefs(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'beliefs': request.data.get('beliefs')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_practices(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'practices': request.data.get('practices')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_origins(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'origins': request.data.get('origins')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_org(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'organization': request.data.get('organization')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_hobj(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'holy_objects': request.data.get('holy_objects')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_holidays(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'holidays': request.data.get('holidays')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PATCH'])
def update_rfigs(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'revered_figures': request.data.get('revered_figures')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_extra(request, pk):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReligionSerializer(religion)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'extra': request.data.get('extra')
        }
        serializer = ReligionSerializer(religion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def religion_edit(request, pk, template_name='religions/edit.html', data={}):
    try:
        religion = Religion.objects.get(pk=pk)
    except Religion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['religion'] = religion
    return render(request, template_name, data)
