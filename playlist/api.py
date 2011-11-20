import logging
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL
from tastypie.resources import ModelResource
from playlist.models import Artist, Album, Track

log = logging.getLogger(__name__)

class ArtistResource(ModelResource):
    class Meta:
        queryset = Artist.objects.all()
        resource_name = 'artists'
        authorization = Authorization()
        filtering = {
            'name': ALL,
            }


class AlbumResource(ModelResource):
    artist = fields.ToOneField('playlist.api.ArtistResource', 'artist')

    class Meta:
        queryset = Album.objects.all()
        resource_name = 'albums'
        authorization = Authorization()
        filtering = {
            'title': ALL,
            }

class TrackResource(ModelResource):
    album = fields.ToOneField('playlist.api.AlbumResource', 'album', full=True)
    class Meta:
        queryset = Track.objects.all()
        resource_name = 'tracks'
        authorization = Authorization()
        filtering = {
            'title': ALL,
            }
