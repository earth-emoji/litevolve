# Generated by Django 2.2 on 2019-05-01 06:50

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('communities', '0003_society_legal'),
        ('accounts', '0002_userprofile_user'),
        ('worlds', '0016_auto_20190426_2131'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('sex', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.CharField(blank=True, max_length=9, null=True)),
                ('birthplace', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('sexual_preference', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('income', models.CharField(blank=True, max_length=9, null=True)),
                ('abilities', tinymce.models.HTMLField(blank=True, null=True)),
                ('relationship_skills', tinymce.models.HTMLField(blank=True, null=True)),
                ('album', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.Album')),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='accounts.UserProfile')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='communities.Religion')),
                ('social_groups', models.ManyToManyField(blank=True, related_name='characters', to='communities.SocialGroup')),
                ('societies', models.ManyToManyField(blank=True, related_name='characters', to='communities.Society')),
                ('species', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='worlds.Species')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('character', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to='characters.Character')),
                ('relation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterPsychology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intelligence', tinymce.models.HTMLField(blank=True, max_length=255, null=True)),
                ('mental_illnesses', tinymce.models.HTMLField(blank=True, null=True)),
                ('learning_experiences', tinymce.models.HTMLField(blank=True, null=True)),
                ('short_term_goals', tinymce.models.HTMLField(blank=True, null=True)),
                ('long_term_goals', tinymce.models.HTMLField(blank=True, null=True)),
                ('self_perception', tinymce.models.HTMLField(blank=True, null=True)),
                ('perceived_by_others', tinymce.models.HTMLField(blank=True, null=True)),
                ('self_confidence', tinymce.models.HTMLField(blank=True, max_length=255, null=True)),
                ('emotionality', tinymce.models.HTMLField(blank=True, null=True)),
                ('shame', tinymce.models.HTMLField(blank=True, null=True)),
                ('mental_strengths', tinymce.models.HTMLField(blank=True, null=True)),
                ('mental_weaknesses', tinymce.models.HTMLField(blank=True, null=True)),
                ('attitude_type', models.CharField(blank=True, choices=[('Extravert', 'Extravert'), ('Introvert', 'Introvert')], max_length=15, null=True)),
                ('deals_with_anger', tinymce.models.HTMLField(blank=True, null=True)),
                ('deals_with_sadness', tinymce.models.HTMLField(blank=True, null=True)),
                ('deals_with_conflict', tinymce.models.HTMLField(blank=True, null=True)),
                ('deals_with_change', tinymce.models.HTMLField(blank=True, null=True)),
                ('deals_with_loss', tinymce.models.HTMLField(blank=True, null=True)),
                ('deals_with_stress', tinymce.models.HTMLField(blank=True, null=True)),
                ('movations', tinymce.models.HTMLField(blank=True, null=True)),
                ('fears', tinymce.models.HTMLField(blank=True, null=True)),
                ('pleasures', tinymce.models.HTMLField(blank=True, null=True)),
                ('extras', tinymce.models.HTMLField(blank=True, null=True)),
                ('character', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterAppearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(blank=True, max_length=10, null=True)),
                ('weight', models.CharField(blank=True, max_length=10, null=True)),
                ('eye_color', models.CharField(blank=True, max_length=20, null=True)),
                ('skin_color', models.CharField(blank=True, max_length=20, null=True)),
                ('face_shape', tinymce.models.HTMLField(blank=True, null=True)),
                ('unique_features', tinymce.models.HTMLField(blank=True, null=True)),
                ('mannerism', tinymce.models.HTMLField(blank=True, null=True)),
                ('habits', tinymce.models.HTMLField(blank=True, null=True)),
                ('health', tinymce.models.HTMLField(blank=True, null=True)),
                ('extra', tinymce.models.HTMLField(blank=True, max_length=20, null=True)),
                ('disabilities', tinymce.models.HTMLField(blank=True, null=True)),
                ('style', tinymce.models.HTMLField(blank=True, max_length=255, null=True)),
                ('character', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
    ]
