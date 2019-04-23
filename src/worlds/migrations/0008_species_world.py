# Generated by Django 2.2 on 2019-04-23 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0007_naturalobject_world'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='world',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='species', to='worlds.World'),
            preserve_default=False,
        ),
    ]
