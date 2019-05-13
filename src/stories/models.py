import uuid
from django.db import models
from tinymce.models import HTMLField

from accounts.models import UserProfile
from characters.models import Character
from photos.models import Album

# Create your models here.
class Story(models.Model):
    GENRE_CHOICES = (
        ('Action/Adventure', 'Action/Adventure'),
        ('Alt-History', 'Alternate History'),
        ('Anthology', 'Anthology'),
        ('Children', 'Children'),
        ('Classic', 'Classic'),
        ('Comic', 'Comic'),
        ('Coming-of-age', 'Coming of age'),
        ('Crime/detective', 'Crime/detective'),
        ('Drama', 'Drama'),
        ('Erotic', 'Erotic'),
        ('Fable', 'Fable'),
        ('Fan fiction', 'Fan fiction'),
        ('Fairytale', 'Fairytale'),
        ('Fantasy', 'Fantasy'),
        ('Graphic novel', 'Graphic novel'),
        ('Historical fiction', 'Historical fiction'),
        ('Horror', 'Horror'),
        ('Humor', 'Humor'),
        ('Legend', 'Legend'),
        ('Magic', 'Magic'),
        ('Meta-fiction', 'Meta-fiction'),
        ('Mystery', 'Mystery'),
        ('Mythology', 'Mythology'),
        ('Mythopoeia', 'Mythopoeia'),
        ('Pictures', 'Pictures'),
        ('Political', 'Political'),
        ('Realistic', 'Realistic'),
        ('Romance', 'Romance'),
        ('Satire', 'Satire'),
        ('Science fiction', 'Science fiction'),
        ('Suspense', 'Suspense'),
        ('Swashbuckler', 'Swashbuckler'),
        ('Thriller', 'Thriller'),
        ('Tall tale', 'Tall tale'),
        ('Western', 'Western'),
        ('Young adult', 'Young adult'),
    )
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    title = models.CharField(max_length=255, blank=True),
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, null=True, blank=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='stories', blank=True)
    characters = models.ManyToManyField(Character, through='StoryCharacter', blank=True)

    def __str__(self):
        return self.title

class StoryCharacter(models.Model):
    ROLE_CHOICE_TYPES = (
        ('Protagonist', 'Protagonist'),
        ('Deuteragonist', 'Deuteragonist'),
        ('Antagonist', 'Antagonist'),
        ('Love Interest', 'Love Interest'),
        ('Mentor', 'Mentor'),
        ('Narrator', 'Narrator'),
        ('Secondary', 'Secondary Character'),
        ('Tertiary', 'Tertiary Character'),
        ('Flat', 'Flat Character'),
    )
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='stories', blank=True)
    arc = HTMLField(null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, blank=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICE_TYPES, null=True, blank=True)

class Premise(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    setting = HTMLField(null=True, blank=True)
    antagonist = models.ForeignKey(StoryCharacter, related_name='antagonist_premises', on_delete=models.CASCADE, null=True, blank=True)
    protagonist = models.ForeignKey(StoryCharacter, related_name='protagonist_premises', on_delete=models.CASCADE, null=True, blank=True)
    ending = HTMLField(null=True, blank=True)
    beginning = HTMLField(null=True, blank=True)
    synopsis = HTMLField(null=True, blank=True)
    story = models.OneToOneField(Story, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='premises', blank=True)

    def __str__(self):
        return self.story.title + "'s Premise"
    
class Plot(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    exposition = HTMLField(null=True, blank=True)
    conflict = HTMLField(null=True, blank=True)
    rising_action = HTMLField(null=True, blank=True)
    climax = HTMLField(null=True, blank=True)
    falling_action = HTMLField(null=True, blank=True)
    resolution = HTMLField(null=True, blank=True)
    story = models.OneToOneField(Story, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='plots', blank=True)

    def __str__(self):
        return self.story.title + "'s Plot"


class Act(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    act_number = models.PositiveIntegerField(blank=True)
    title = models.CharField(max_length=255)
    overview = HTMLField(null=True, blank=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='acts', blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='acts', blank=True)
    
    def __str__(self):
        return self.title


class Chapter(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    chap_number = models.PositiveIntegerField(blank=True)
    title = models.CharField(max_length=255, blank=True)
    overview = HTMLField(null=True, blank=True)
    act = models.ForeignKey(Act, on_delete=models.CASCADE, related_name='chapters', blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='chapters', blank=True)

    def __str__(self):
        return self.title


class Scene(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    title = models.CharField(max_length=255, blank=True)
    goal = HTMLField(null=True, blank=True)
    emotion = HTMLField(null=True, blank=True)
    setting = HTMLField(null=True, blank=True)
    pov = models.CharField(max_length=255, null=True, blank=True)
    action = HTMLField(null=True, blank=True)
    position = models.PositiveIntegerField(default=0, blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='scenes', blank=True)
    characters = models.ManyToManyField(Character, related_name='scenes', blank=True)

    def __str__(self):
        return self.title

class Dialogue(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, related_name='dialogues', blank=True)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='dialogues', blank=True)
    content = HTMLField(blank=True)
