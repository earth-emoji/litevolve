from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(models.Manager):
    use_for_related_fields = True

# Create your models here. 
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)

    objects = UserProfileManager()

    def __str__(self):
        return self.user.username

