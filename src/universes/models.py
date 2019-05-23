import uuid
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from tinymce.models import HTMLField

from accounts.models import UserProfile
from projects.models import Task


# Create your models here.
VISIBILITY_CHOICES = (
    ('Private', 'Private'),
    ('Collaborators', 'Collaborators'),
    ('Group', 'Group'),
    ('Public', 'Public')
)


class Universe(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    overview = HTMLField(null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    tasks = GenericRelation(Task)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='universes', blank=True)

    def __str__(self):
        return self.name

    @property
    def url(self):
        return "/universes/view/%s/" %(self.slug)


class NaturalLaw(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    can = HTMLField(null=True, blank=True)
    cannot = HTMLField(null=True, blank=True)
    explanation = HTMLField(null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    universes = models.ManyToManyField(
        Universe, related_name='natural_laws', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='natural_laws', blank=True)

    def __str__(self):
        return self.name

    @property
    def url(self):
        return "/natural_laws/view/%s/" %(self.slug)


class Particle(models.Model):
    PARTICLE_SIZE_CHOICES = (
        ('Subatomic', 'Subatomic'),
        ('Microscopic', 'Microscopic'),
        ('Macroscopic', 'Macroscopic'),
    )
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    size = models.CharField(
        max_length=11, choices=PARTICLE_SIZE_CHOICES, null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    is_stable = models.BooleanField(default=True)
    composition = models.ManyToManyField('self', blank=True)
    universes = models.ManyToManyField(
        Universe, related_name='particles', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='particles', blank=True)

    def __str__(self):
        return self.name


class Element(models.Model):
    MATTER_STATE_CHOICES = (
        ('Gas', 'Gas'),
        ('Liquid', 'Liquid'),
        ('Solid', 'Solid'),
        ('Unknown', 'Unknown'),
    )
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    matter_state = models.CharField(
        max_length=25, choices=MATTER_STATE_CHOICES, null=True, blank=True)
    is_metal = models.BooleanField(default=False)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    universes = models.ManyToManyField(
        Universe, related_name='elements', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='elements', blank=True)

    def __str__(self):
        return self.name

    def add(num, num2):
        return num + num2


class CelestialBody(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    universes = models.ManyToManyField(
        Universe, related_name='celestial_bodies', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='celestial_bodies', blank=True)

    def __str__(self):
        return self.name


class NaturalPhenomena(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    celestial_bodies = models.ManyToManyField(
        CelestialBody, related_name='natural_phenomenas', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='natural_phenomenas', blank=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    span = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    celestial_bodies = models.ManyToManyField(
        CelestialBody, related_name='seasons', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='seasons', blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    scenery = HTMLField(null=True, blank=True)
    description = HTMLField(null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    celestial_bodies = models.ManyToManyField(
        CelestialBody, related_name='places', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='places', blank=True)
    seasons = models.ManyToManyField(
        Season, related_name='places', through='PlaceSeason', blank=True)

    def __str__(self):
        return self.name


class PlaceSeason(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    weather = HTMLField(null=True, blank=True)


class NaturalObject(models.Model):
    VALUE_CHOICES = (
        ('High', 'High'),
        ('Average', 'Average'),
        ('Low', 'Low'),
        ('None', 'None'),
    )
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    appearance = HTMLField(null=True, blank=True)
    history = HTMLField(null=True, blank=True)
    value = models.CharField(max_length=255, null=True,
                             blank=True, choices=VALUE_CHOICES)
    value_description = HTMLField(null=True, blank=True)
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    places = models.ManyToManyField(
        Place, related_name='natural_objects', blank=True)
    celestial_bodies = models.ManyToManyField(
        CelestialBody, related_name='natural_objects', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='natural_objects', blank=True)

    def __str__(self):
        return self.name


class Species(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
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
    visibility = models.CharField(
        default='Private', max_length=13, choices=VISIBILITY_CHOICES, blank=True)
    places = models.ManyToManyField(Place, related_name='species', blank=True)
    celestial_bodies = models.ManyToManyField(
        CelestialBody, related_name='species', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='species', blank=True)

    def __str__(self):
        return self.name
