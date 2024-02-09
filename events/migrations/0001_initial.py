# Generated by Django 5.0.1 on 2024-02-09 04:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='events/attachments/')),
                ('description', models.TextField(max_length=50)),
                ('content', models.TextField(max_length=1000)),
                ('level', models.TextField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('P', 'Professional')])),
                ('age_group', models.TextField(choices=[('C', 'Children'), ('T', 'Teenagers'), ('A', 'Adults'), ('S', 'Seniors')])),
                ('max_players', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('admins', models.ManyToManyField(blank=True, related_name='admin_events', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('sport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.sport')),
            ],
        ),
    ]
