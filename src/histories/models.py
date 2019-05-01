from django.db import models
from tinymce.models import HTMLField

from accounts.models import UserProfile
from characters.models import Character
from communities.models import Society, Religion, SocialGroup
from worlds.models import World, Place, Species, CelestialBody


# Create your models here.
class History(models.Model):
    name = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    description = HTMLField(null=True, blank=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    celestial_body = models.ForeignKey(CelestialBody, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    society = models.ForeignKey(Society, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    social_group = models.ForeignKey(SocialGroup, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='histories', null=True, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='histories', blank=True)

    def __str__(self):
        return self.name
