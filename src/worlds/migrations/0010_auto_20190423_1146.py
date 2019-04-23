# Generated by Django 2.2 on 2019-04-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0009_species_ecosystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celestialbody',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='celestial_bodies', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='celestialbody',
            name='world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='celestial_bodies', to='worlds.World'),
        ),
        migrations.AlterField(
            model_name='history',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='infrastructure',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='infrastructures', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='naturalobject',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='natural_objects', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='naturalobject',
            name='world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='natural_objects', to='worlds.World'),
        ),
        migrations.AlterField(
            model_name='naturalphenomena',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='natural_phenomenas', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='naturalphenomena',
            name='world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='natural_phenomenas', to='worlds.World'),
        ),
        migrations.AlterField(
            model_name='place',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='place',
            name='world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='places', to='worlds.World'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='religions', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='worlds.World'),
        ),
        migrations.AlterField(
            model_name='season',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='season',
            name='world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='worlds.World'),
        ),
        migrations.AlterField(
            model_name='socialgroup',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_groups', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='socialgroup',
            name='society',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='social_groups', to='worlds.Society'),
        ),
        migrations.AlterField(
            model_name='society',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='societies', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='species',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='species', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='species',
            name='world',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='species', to='worlds.World'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='accounts.UserProfile'),
        ),
    ]
