# Generated by Django 2.2 on 2019-04-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0011_auto_20190423_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naturalobject',
            name='value',
            field=models.CharField(blank=True, choices=[('High', 'High'), ('Average', 'Average'), ('Low', 'Low'), ('None', 'None')], max_length=255, null=True),
        ),
    ]