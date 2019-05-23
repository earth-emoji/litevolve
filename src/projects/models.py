import uuid

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import UserProfile
from utils import obj, calc

# Create your models here.

class ProjectManager(models.Manager):
    def ctasks(self, creator, slug):
        return self.filter(slug=slug,tasks__is_complete=True, creator=creator)

    def ctasks_count(self, creator, slug):
        return self.filter(slug=slug, tasks__is_complete=True, creator=creator).exclude().count()

class Project(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    day = models.DateField(blank=True)
    start = models.DateTimeField(**obj.NULL_AND_BLANK)
    end = models.DateTimeField(**obj.NULL_AND_BLANK)
    details = models.TextField(**obj.NULL_AND_BLANK)
    is_complete = models.BooleanField(default=False, blank=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='projects', blank=True)

    objects = ProjectManager()

    def __str__(self):
       return self.name

    @property
    def progress(self):
        tasks = self.tasks.count()
        ctasks = Project.objects.ctasks_count(slug=self.slug, creator=self.creator)
        progress = calc.get_progress(goal=tasks, completed=ctasks)
        # print(tasks)
        # print(ctasks)
        return progress


class Task(models.Model):
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    name = models.CharField(max_length=255, blank=True)
    day = models.DateField(blank=True)
    start = models.DateTimeField(**obj.NULL_AND_BLANK)
    end = models.DateTimeField(**obj.NULL_AND_BLANK)
    details = models.TextField(**obj.NULL_AND_BLANK)
    is_complete = models.BooleanField(default=False, blank=True)
    #collaborators = models.ManyToManyField(UserProfile, related_name='tasks', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', blank=True)
    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, **obj.NULL_AND_BLANK)
    object_id = models.PositiveIntegerField(**obj.NULL_AND_BLANK)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name
