from django.db import models
import logging

log = logging.getLogger(__name__)

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Album(models.Model):
    title = models.CharField(max_length=255)

    artist = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Track(models.Model):
    track_number = models.IntegerField()
    title = models.CharField(max_length=255)

    album = models.ForeignKey(Album)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['track_number']