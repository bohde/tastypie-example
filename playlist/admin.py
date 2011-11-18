from django.contrib import admin
from playlist.models import Artist, Album, Track

class ArtistAdmin(admin.ModelAdmin):
    pass
class AlbumAdmin(admin.ModelAdmin):
    pass
class TrackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)