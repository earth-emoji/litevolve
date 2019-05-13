from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets

from accounts.models import UserProfile
from stories.models import Story
from stories.serializers import StorySerializer

class StoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Story.objects.filter(author=request.user.profile)
        serializer = StorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, slug=None):
        queryset = Story.objects.filter(author=request.user.profile)
        story = get_object_or_404(queryset, slug=slug)
        serializer = StorySerializer(story)
        return Response(serializer.data)


    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
