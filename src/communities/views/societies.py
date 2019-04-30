from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from communities.models import Society, SocialGroup, Religion
from communities.serializers import SocietySerializer
from histories.models import History
from histories.serializers import HistorySerializer
from worlds.models import World, Species, Place
from accounts.models import UserProfile


# Create your views here.
def index(request, pk, template_name='societies/index.html', data={}):
    data['creator'] = UserProfile.objects.get(pk=pk, user=request.user)
    return render(request, template_name, data)


@api_view(['GET', 'POST'])
def society_collection(request):
    if request.method == 'GET':
        societies = Society.objects.filter(creator=request.user.profile)
        serializer = SocietySerializer(societies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = SocietySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def society_single(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        society.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_type(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'type': request.data.get('type')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_gov(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'government': request.data.get('government')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_lead(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'leadership': request.data.get('leadership')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_military(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'military': request.data.get('military')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_social_capital(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'social_capital': request.data.get('social_capital')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_hierarchy(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'hierarchy': request.data.get('hierarchy')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_origin(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'origin': request.data.get('origin')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_economy(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'economy': request.data.get('economy')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_legal(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'legal': request.data.get('legal')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_rivals(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'rivals': request.data.get('rivals')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_extra(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocietySerializer(society)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'extra': request.data.get('extra')
        }
        serializer = SocietySerializer(society, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def society_edit(request, pk, template_name='societies/edit.html', data={}):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['society'] = society
    return render(request, template_name, data)
