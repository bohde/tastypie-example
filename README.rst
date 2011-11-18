=====================================================
Problem Description
=====================================================

I am trying to create an api for consumption by my own app via backbone.js.
I have the need to display attributes of related resources (read only) in many of my views.

In this example I have an albums resource and a tracks resource (also artists - but we can exclude that for now).
I want to display a listing of tracks along with the album name - each track may be from a different album.
By default `album = fields.ToOneField('AlbumResource', 'album')` will only give me the url so I cannot grab the album name without additional http requests and stitching the data back together.
On the other hand if I use `album = fields.ToOneField('AlbumResource', 'album', full=True)` I get the album information which is good.
The problem is that the resulting json can not be put back to the server to be updated (it simply will not work - it appears tasty is not designed to do this, which is probably the right thing).

What is the best way to do this?
I want extra read only attributes of a related resources but also what to be able to use the same resource for updating.

Installation
------------
Install requirements with ``pip``::

     pip install -r requirements.txt

Sync the database::

     ./manage.py syncdb

Additional Info
---------------
Specifics of the issue can be found by running the app and pointing to the index page @ http://127.0.0.1:8000