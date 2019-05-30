# Generated by Django 2.2 on 2019-05-25 05:29

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_user'),
        ('universes', '0005_delete_compound'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('visibility', models.CharField(blank=True, choices=[('Private', 'Private'), ('Collaborators', 'Collaborators'), ('Group', 'Group'), ('Public', 'Public')], default='Private', max_length=13)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dimensions', to='accounts.UserProfile')),
                ('universes', models.ManyToManyField(blank=True, related_name='dimensions', to='universes.Universe')),
            ],
        ),
    ]
