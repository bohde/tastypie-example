from django.conf.urls.defaults import *
from tastypie.api import Api
from playlist.api import ArtistResource, AlbumResource, TrackResource

api_v1 = Api(api_name='v1')
api_v1.register(ArtistResource())
api_v1.register(AlbumResource())
api_v1.register(TrackResource())

urlpatterns = patterns('playlist.views',
                       url(r'^api/', include(api_v1.urls)),
                       )