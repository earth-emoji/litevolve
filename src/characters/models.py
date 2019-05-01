from django.db import models
from tinymce.models import HTMLField

from accounts.models import UserProfile
from communities.models import Society, SocialGroup, Religion
from photos.models import Album
from worlds.models import Species


# Create your models here.
class Character(models.Model):

    name = models.CharField(max_length=255, blank=True)
    sex = models.CharField(max_length=30, null=True, blank=True)
    age = models.CharField(max_length=9, null=True, blank=True)
    birthplace = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    sexual_preference = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    income = models.CharField(max_length=9, null=True, blank=True)
    abilities = HTMLField(blank=True, null=True)
    relationship_skills = HTMLField(blank=True, null=True)

    album = models.OneToOneField(
        Album, on_delete=models.CASCADE, null=True, blank=True)
    societies = models.ManyToManyField(
        Society, related_name='characters', blank=True)
    social_groups = models.ManyToManyField(
        SocialGroup, related_name="characters", blank=True)
    religion = models.ManyToManyField(
        Religion, related_name="characters", blank=True)
    species = models.ForeignKey(
        Species, on_delete=models.CASCADE, related_name='characters', blank=True)
    creator = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='characters', blank=True)

    def __str__(self):
        return self.name


class CharacterAppearance(models.Model):
    height = models.CharField(max_length=10, null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    eye_color = models.CharField(max_length=20, null=True, blank=True)
    skin_color = models.CharField(max_length=20, null=True, blank=True)
    face_shape = HTMLField(null=True, blank=True)
    unique_features = HTMLField(null=True, blank=True)
    mannerism = HTMLField(null=True, blank=True)
    habits = HTMLField(null=True, blank=True)
    health = HTMLField(null=True, blank=True)
    extra = HTMLField(max_length=20, null=True, blank=True)
    disabilities = HTMLField(null=True, blank=True)
    style = HTMLField(max_length=255, null=True, blank=True)
    character = models.OneToOneField(
        Character, on_delete=models.CASCADE, blank=True)


class CharacterPsychology(models.Model):
    ATTITUDE_TYPE_CHOICES = (
        ('Extravert', 'Extravert'),
        ('Introvert', 'Introvert')
    )

    intelligence = HTMLField(max_length=255, null=True, blank=True)
    mental_illnesses = HTMLField(null=True, blank=True)
    learning_experiences = HTMLField(null=True, blank=True)
    short_term_goals = HTMLField(null=True, blank=True)
    long_term_goals = HTMLField(null=True, blank=True)
    self_perception = HTMLField(null=True, blank=True)
    perceived_by_others = HTMLField(null=True, blank=True)
    self_confidence = HTMLField(max_length=255, null=True, blank=True)
    emotionality = HTMLField(null=True, blank=True)
    shame = HTMLField(null=True, blank=True)
    mental_strengths = HTMLField(null=True, blank=True)
    mental_weaknesses = HTMLField(null=True, blank=True)
    attitude_type = models.CharField(
        max_length=15, choices=ATTITUDE_TYPE_CHOICES, null=True, blank=True)
    deals_with_anger = HTMLField(null=True, blank=True)
    deals_with_sadness = HTMLField(null=True, blank=True)
    deals_with_conflict = HTMLField(null=True, blank=True)
    deals_with_change = HTMLField(null=True, blank=True)
    deals_with_loss = HTMLField(null=True, blank=True)
    deals_with_stress = HTMLField(null=True, blank=True)
    movations = HTMLField(null=True, blank=True)
    fears = HTMLField(null=True, blank=True)
    pleasures = HTMLField(null=True, blank=True)
    extras = HTMLField(null=True, blank=True)
    character = models.OneToOneField(
        Character, on_delete=models.CASCADE, blank=True)


class CharacterRelationship(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.CASCADE, related_name='relationships', blank=True)
    relation = models.ForeignKey(
        Character, on_delete=models.CASCADE, blank=True)
    description = HTMLField(blank=True)
