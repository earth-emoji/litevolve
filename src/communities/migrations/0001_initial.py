# Generated by Django 2.2 on 2019-04-25 05:40

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('worlds', '0014_auto_20190424_2240'),
        ('accounts', '0002_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('type', tinymce.models.HTMLField(blank=True, null=True)),
                ('government', tinymce.models.HTMLField(blank=True, null=True)),
                ('leadership', tinymce.models.HTMLField(blank=True, null=True)),
                ('military', tinymce.models.HTMLField(blank=True, null=True)),
                ('social_capital', tinymce.models.HTMLField(blank=True, null=True)),
                ('hierarchy', tinymce.models.HTMLField(blank=True, null=True)),
                ('origin', tinymce.models.HTMLField(blank=True, null=True)),
                ('economy', tinymce.models.HTMLField(blank=True, null=True)),
                ('rivals', tinymce.models.HTMLField(blank=True, null=True)),
                ('extra', tinymce.models.HTMLField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='societies', to='accounts.UserProfile')),
                ('places', models.ManyToManyField(blank=True, related_name='societies', to='worlds.Place')),
                ('species', models.ManyToManyField(blank=True, related_name='societies', to='worlds.Species')),
            ],
        ),
        migrations.CreateModel(
            name='SocialGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('type', tinymce.models.HTMLField(blank=True, null=True)),
                ('goals', tinymce.models.HTMLField(blank=True, null=True)),
                ('structure', tinymce.models.HTMLField(blank=True, null=True)),
                ('cohesiveness', tinymce.models.HTMLField(blank=True, null=True)),
                ('extra', tinymce.models.HTMLField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_groups', to='accounts.UserProfile')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_groups', to='communities.SocialGroup')),
                ('society', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_groups', to='communities.Society')),
                ('species', models.ManyToManyField(blank=True, related_name='social_groups', to='worlds.Species')),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('deities', tinymce.models.HTMLField(blank=True, null=True)),
                ('beliefs', tinymce.models.HTMLField(blank=True, null=True)),
                ('practices', tinymce.models.HTMLField(blank=True, null=True)),
                ('origins', tinymce.models.HTMLField(blank=True, null=True)),
                ('organization', tinymce.models.HTMLField(blank=True, null=True)),
                ('holy_objects', tinymce.models.HTMLField(blank=True, null=True)),
                ('holidays', tinymce.models.HTMLField(blank=True, null=True)),
                ('revered_figures', tinymce.models.HTMLField(blank=True, null=True)),
                ('extra', tinymce.models.HTMLField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='religions', to='accounts.UserProfile')),
                ('places', models.ManyToManyField(blank=True, related_name='religions', to='worlds.Place')),
                ('societies', models.ManyToManyField(blank=True, related_name='religions', to='communities.Society')),
                ('species', models.ManyToManyField(blank=True, related_name='religions', to='worlds.Species')),
            ],
        ),
    ]
