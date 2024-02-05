from django.db import models


# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Attachment(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments/')
    event = models.ForeignKey('Event', related_name='attachments', on_delete=models.CASCADE)


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    sports = models.ManyToManyField(Sport)
    players = models.ManyToManyField('auth.User') # TODO: Need to be edit after merging with user app
    max_players = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE) # TODO: Need to be edit after merging with user app
    admins = models.ManyToManyField('auth.User', related_name='admin_events') # TODO: Need to be edit after merging with user app
