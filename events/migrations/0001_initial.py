# Generated by Django 5.0.1 on 2024-03-23 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ('description', models.TextField(max_length=1000)),
                ('content', models.TextField()),
                ('level', models.TextField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced'), ('P', 'Professional')])),
                ('age_group', models.TextField(choices=[('C', 'Children'), ('T', 'Teenagers'), ('A', 'Adults'), ('S', 'Seniors')])),
                ('visibility', models.TextField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Public')),
                ('max_players', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('promotion', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('admins', models.ManyToManyField(blank=True, related_name='admin_events', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_events', to=settings.AUTH_USER_MODEL)),
                ('players', models.ManyToManyField(blank=True, related_name='join_events', to=settings.AUTH_USER_MODEL)),
                ('sport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='accounts.sport')),
            ],
        ),
    ]
