# Generated by Django 2.2 on 2019-04-27 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0015_auto_20190426_1950'),
        ('communities', '0001_initial'),
        ('histories', '0002_auto_20190424_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='history',
            name='object_id',
        ),
        migrations.AddField(
            model_name='history',
            name='celestial_body',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='worlds.CelestialBody'),
        ),
        migrations.AddField(
            model_name='history',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='worlds.Place'),
        ),
        migrations.AddField(
            model_name='history',
            name='religion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='communities.Religion'),
        ),
        migrations.AddField(
            model_name='history',
            name='social_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='communities.SocialGroup'),
        ),
        migrations.AddField(
            model_name='history',
            name='society',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='communities.Society'),
        ),
        migrations.AddField(
            model_name='history',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='worlds.Species'),
        ),
        migrations.AddField(
            model_name='history',
            name='world',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='worlds.World'),
        ),
    ]
