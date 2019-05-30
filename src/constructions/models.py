from django.db import models
from tinymce.models import HTMLField

from accounts.models import UserProfile
from communities.models import Society
from universes.models import Place

# Create your models here.
# art, attire


class Technology(models.Model):
    name = models.CharField(max_length=255, blank=True)
    appearance = HTMLField(null=True, blank=True)
    utility = HTMLField(null=True, blank=True)
    origins = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    societies = models.ManyToManyField(
        Society, related_name='technologies', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='technologies', blank=True)

    def __str__(self):
        return self.name


class Infrastructure(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = HTMLField(null=True, blank=True)
    appearance = HTMLField(null=True, blank=True)
    purpose = HTMLField(null=True, blank=True)
    origins = HTMLField(null=True, blank=True)
    extra = HTMLField(null=True, blank=True)
    places = models.ManyToManyField(
        Place, related_name='infrastructures', blank=True)
    societies = models.ManyToManyField(
        Society, related_name='infrastructures', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='infrastructures', blank=True)

    def __str__(self):
        return self.name
