# Generated by Django 2.2 on 2019-04-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialgroup',
            name='society',
        ),
        migrations.AddField(
            model_name='socialgroup',
            name='society',
            field=models.ManyToManyField(blank=True, related_name='social_groups', to='communities.Society'),
        ),
    ]
