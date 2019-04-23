from django.db import models
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
    background = HTMLField(null=True, blank=True)
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
        ('Highly', 'Highly'),
        ('Average', 'Average'),
        ('Barely', 'Barely'),
        ('No', 'No'),
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
    origins = HTMLField(null=True, blank=True)
    habitat = HTMLField(null=True, blank=True)
    ecosystem = HTMLField(null=True, blank=True)
    diet = HTMLField(null=True, blank=True)
    predators = HTMLField(null=True, blank=True)
    defense = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    is_intelligent  = models.BooleanField(default=False)
    places = models.ManyToManyField(Place, related_name='species', blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='species', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='species', blank=True)

    def __str__(self):
        return self.name

class Society(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = HTMLField(null=True, blank=True)
    government = HTMLField(null=True, blank=True)
    leadership = HTMLField(null=True, blank=True)
    military = HTMLField(null=True, blank=True)
    social_capital = HTMLField(null=True, blank=True)
    hierarchy = HTMLField(null=True, blank=True)
    origin = HTMLField(null=True, blank=True)
    economy = HTMLField(null=True, blank=True)
    rivals = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    species = models.ManyToManyField(Species, related_name='societies', blank=True)
    places = models.ManyToManyField(Place, related_name='societies', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='societies', blank=True)

    def __str__(self):
        return self.name

class SocialGroup(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = HTMLField(null=True, blank=True)
    goals = HTMLField(null=True, blank=True)
    structure = HTMLField(null=True, blank=True)
    cohesiveness = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_groups', null=True, blank=True)
    species = models.ManyToManyField(Species, related_name='social_groups', blank=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name='social_groups', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='social_groups', blank=True)    

    def __str__(self):
        return self.name

class Religion(models.Model):
    name = models.CharField(max_length=255, blank=True)
    deities = HTMLField(null=True, blank=True)
    beliefs = HTMLField(null=True, blank=True)
    practices = HTMLField(null=True, blank=True)
    origins = HTMLField(null=True, blank=True)
    organization = HTMLField(null=True, blank=True)
    holy_objects = HTMLField(null=True, blank=True)
    holidays = HTMLField(null=True, blank=True)
    revered_figures = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    species = models.ManyToManyField(Species, related_name='religions', blank=True)
    places = models.ManyToManyField(Place, related_name='religions', blank=True)
    societies = models.ManyToManyField(Society, related_name='religions', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='religions', blank=True)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=255, blank=True)
    appearance = HTMLField(null=True, blank=True)
    utility = HTMLField(null=True, blank=True)
    practices = HTMLField(null=True, blank=True)
    origins = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    societies = models.ManyToManyField(Society, related_name='technologies', blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='technologies', blank=True)

    def __str__(self):
        return self.name

class Infrastructure(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = HTMLField(null=True, blank=True)
    appearance = HTMLField(null=True, blank=True)
    purpose = HTMLField(null=True, blank=True)
    origins = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='infrastructures', null=True, blank=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name='infrastructures', null=True, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='infrastructures', blank=True)

    def __str__(self):
        return self.name

class History(models.Model):
    name = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    social_group = models.ForeignKey(SocialGroup, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    infrastructure = models.ForeignKey(Infrastructure, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='histories', blank=True)

    def __str__(self):
        return self.name