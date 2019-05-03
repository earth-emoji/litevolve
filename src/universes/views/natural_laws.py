from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from universes.models import NaturalLaw
from universes.serializers import NaturalLawSerializer


@api_view(['GET', 'POST'])
def rule_collection(request):
    if request.method == 'GET':
        rules = NaturalLaw.objects.filter(creator=request.user.profile)
        serializer = NaturalLawSerializer(rules, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'creator': request.user.profile.pk
        }
        serializer = NaturalLawSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def rule_single(request, slug):
    try:
        rule = NaturalLaw.objects.get(slug=slug)
    except NaturalLaw.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalLawSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        rule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def update_can(request, slug):
    try:
        rule = NaturalLaw.objects.get(slug=slug)
    except NaturalLaw.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalLawSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'can': request.data.get('can')
        }
        serializer = NaturalLawSerializer(rule, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_cannot(request, slug):
    try:
        rule = NaturalLaw.objects.get(slug=slug)
    except NaturalLaw.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalLawSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'cannot': request.data.get('cannot')
        }
        serializer = NaturalLawSerializer(rule, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH'])
def update_explanation(request, slug):
    try:
        rule = NaturalLaw.objects.get(slug=slug)
    except NaturalLaw.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NaturalLawSerializer(rule)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        data = {
            'explanation': request.data.get('explanation')
        }
        serializer = NaturalLawSerializer(rule, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def rule_edit(request, slug, template_name='rules/edit.html', data={}):
    try:
        rule = NaturalLaw.objects.get(slug=slug)
    except NaturalLaw.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data['rule'] = rule
    return render(request, template_name, data)
