# Generated by Django 2.2 on 2019-05-21 21:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
    ]