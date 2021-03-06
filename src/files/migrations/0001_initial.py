# Generated by Django 2.2 on 2019-05-03 09:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=500, null=True)),
                ('file_type', models.CharField(max_length=100, null=True)),
                ('size', models.IntegerField(null=True)),
                ('file', models.FileField(upload_to='docs')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share_history', to='files.File')),
                ('recipients', models.ManyToManyField(related_name='files_recieved', to='accounts.UserProfile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files_shared', to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='accounts.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='files.Folder'),
        ),
    ]
