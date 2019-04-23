from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from worlds.models import Rule, World
from worlds.serializers import RuleSerializer

@api_view(['GET', 'POST'])
def rule_collection(request, pk):
    world = World.objects.get(pk=pk)
    if request.method == 'GET':
        rules = Rule.objects.filter(world=world)
        serializer = RuleSerializer(rules, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'), 
            'world': world.pk,
            'creator': request.user.profile.pk
        }
        serializer = RuleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def rule_single(request, pk):
    try:
        rule = Rule.objects.get(pk=pk)
    except Rule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RuleSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        rule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PATCH'])
def update_can(request, pk):
    try:
        rule = Rule.objects.get(pk=pk)
    except Rule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RuleSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'can': request.data.get('can')
        }
        serializer = RuleSerializer(rule, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_cannot(request, pk):
    try:
        rule = Rule.objects.get(pk=pk)
    except Rule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RuleSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'cannot': request.data.get('cannot')
        }
        serializer = RuleSerializer(rule, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH'])
def update_explanation(request, pk):
    try:
        rule = Rule.objects.get(pk=pk)
    except Rule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = RuleSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'explanation': request.data.get('explanation')
        }
        serializer = RuleSerializer(rule, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def rule_edit(request, pk, template_name='rules/edit.html', data={}):
    try:
        rule = Rule.objects.get(pk=pk)
    except Rule.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['rule'] = rule
    return render(request, template_name, data)

    