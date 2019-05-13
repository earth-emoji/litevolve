import uuid
from django.db import models
from tinymce.models import HTMLField

from accounts.models import UserProfile
from universes.models import Place, Species

# Create your models here.


class Society(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    type = HTMLField(null=True, blank=True)
    government = HTMLField(null=True, blank=True)
    leadership = HTMLField(null=True, blank=True)
    military = HTMLField(null=True, blank=True)
    social_capital = HTMLField(null=True, blank=True)
    hierarchy = HTMLField(null=True, blank=True)
    origin = HTMLField(null=True, blank=True)
    economy = HTMLField(null=True, blank=True)
    legal = HTMLField(null=True, blank=True)
    rivals = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    species = models.ManyToManyField(
        Species, related_name='societies', blank=True)
    places = models.ManyToManyField(
        Place, related_name='societies', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='societies', blank=True)

    def __str__(self):
        return self.name


class SocialGroup(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    type = HTMLField(null=True, blank=True)
    goals = HTMLField(null=True, blank=True)
    structure = HTMLField(null=True, blank=True)
    cohesiveness = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='sub_groups', null=True, blank=True)
    species = models.ManyToManyField(
        Species, related_name='social_groups', blank=True)
    society = models.ManyToManyField(
        Society, related_name='social_groups', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='social_groups', blank=True)

    def __str__(self):
        return self.name


class Religion(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
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
    species = models.ManyToManyField(
        Species, related_name='religions', blank=True)
    places = models.ManyToManyField(
        Place, related_name='religions', blank=True)
    societies = models.ManyToManyField(
        Society, related_name='religions', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='religions', blank=True)

    def __str__(self):
        return self.name
