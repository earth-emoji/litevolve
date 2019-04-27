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