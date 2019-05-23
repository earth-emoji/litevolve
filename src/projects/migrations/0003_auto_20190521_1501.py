# Generated by Django 2.2 on 2019-05-21 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190521_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='task',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
