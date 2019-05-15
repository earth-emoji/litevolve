# Generated by Django 2.2 on 2019-05-13 02:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='act',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AddField(
            model_name='dialogue',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid1, unique=True),
        ),
    ]