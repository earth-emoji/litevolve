from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from tinymce.models import HTMLField

from accounts.models import UserProfile

# Create your models here.
class World(models.Model):
    name = models.CharField(max_length=255, blank=True)
    overview = HTMLField(null=True, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='worlds')

    def __str__(self):
        return self.name
    
class Rule(models.Model):
    name = models.CharField(max_length=255, blank=True)
    can = HTMLField(null=True, blank=True)
    cannot = HTMLField(null=True, blank=True)
    explanation = HTMLField(null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='rules', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='rules', blank=True)

    def __str__(self):
        return self.name

class CelestialBody(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='celestial_bodies', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='celestial_bodies', blank=True)

    def __str__(self):
        return self.name

class NaturalPhenomena(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='natural_phenomenas', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='natural_phenomenas', blank=True)

    def __str__(self):
        return self.name

class Season(models.Model):
    name = models.CharField(max_length=255, blank=True)
    span = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='seasons', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='seasons', blank=True)
    
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255, blank=True)
    scenery = HTMLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='places', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='places', blank=True)
    seasons = models.ManyToManyField(Season, related_name='seasons', through='PlaceSeason')

    def __str__(self):
        return self.name

class PlaceSeason(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='places')
    weather = HTMLField(null=True, blank=True)

class NaturalObject(models.Model):
    VALUE_CHOICES = (
        ('High', 'High'),
        ('Average', 'Average'),
        ('Low', 'Low'),
        ('None', 'None'),
    )
    name = models.CharField(max_length=255, blank=True)
    appearance = HTMLField(null=True, blank=True)
    history = HTMLField(null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True, choices=VALUE_CHOICES)
    value_description = HTMLField(null=True, blank=True)
    places = models.ManyToManyField(Place, related_name='natural_objects', blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='natural_objects', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='natural_objects', blank=True)

    def __str__(self):
        return self.name

class Species(models.Model):
    name = models.CharField(max_length=255, blank=True)
    appearance = HTMLField(null=True, blank=True)
    unique_abilities = HTMLField(null=True, blank=True)
    intelligence = HTMLField(null=True, blank=True)
    origins = HTMLField(null=True, blank=True)
    habitat = HTMLField(null=True, blank=True)
    ecosystem = HTMLField(null=True, blank=True)
    diet = HTMLField(null=True, blank=True)
    predators = HTMLField(null=True, blank=True)
    defense = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    places = models.ManyToManyField(Place, related_name='species', blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='species', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='species', blank=True)

    def __str__(self):
        return self.name
