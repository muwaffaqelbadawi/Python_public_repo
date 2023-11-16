***


example of random unfiltered data
# Ariana Grande - break up with your girlfriend_ i_m(MP3_128K).mp3


Song Object properties:
    title, subtitle, album, year, genre, capacity, bitrate, sampleRate


Artist Object properties: 
    name, soloSongs, featuringSongs, albums



# Song
[
  {
    title: "title",
    genre: "genre",
    year: "year",
    bitrate: "128kb/160kp",
    sampleRate: "44.1 KHz"
  },
  {
    title: "title",
    genre: "genre",
    year: "year",
    size:"size",
    bitrate: "128kb/160kp",
    sampleRate: "44.1 KHz"
  },
  {
    title: "title",
    genre: "genre",
    year: "year",
    size:"size",
    bitrate: "128kb/160kp",
    sampleRate: "44.1KHz"
  }
]



# Artist
[
  {
    artist: "artist",
    albumArtist: "album artist"
  },
  {
    artist: "artist",
    albumArtist: "album artist"
  },
  {
    artist: "artist",
    albumArtist: "album artist"
  }
]


# Album
[
  {
    album: "album"
  }
]


# Folder
[
  {
    size:"size"
  }
]



>>> path = r'D:\mp3\12 Stones\2002 - 12 Stones\01 - Crash.mp3'
>>> from mutagen.id3 import ID3
>>> audio = ID3(path)
>>> audio
>>> audio['TPE1']
TPE1(encoding=0, text=[u'12 Stones'])
>>> audio['TPE1'].text
[u'12 Stones']
Here’s a more proper example:

from mutagen.id3 import ID3
 
#----------------------------------------------------------------------
def getMutagenTags(path):
    """"""
    audio = ID3(path)
 
    print "Artist: %s" % audio['TPE1'].text[0]
    print "Track: %s" % audio["TIT2"].text[0]
    print "Release Year: %s" % audio["TDRC"].text[0]
I personally find this to be difficult to read and use, so I won’t be using this module for my mp3 player unless I need to add additional digital file formats to it. Also note that I wasn’t able to figure out how to get the track’s play length or album title. Let’s move on to our next ID3 parser and see how it fares.

eyeD3
If you go to eyeD3’s website, you’ll notice that it doesn’t seem to support Windows. This is a problem for many users and almost caused me to drop it from this round-up. Fortunately, I found a forum that mentioned a way to make it work. The idea was to rename the “setup.py.in” file in the main folder to just “setup.py” and the “__init__.py.in” file to “__init__.py”, which you’ll find in “src\eyeD3”. Then you can install it using the usual “python setup.py install”. Once you have it installed, it’s really easy to use. Check out the following function:

import eyeD3
 
#----------------------------------------------------------------------
def getEyeD3Tags(path):
    """"""
    trackInfo = eyeD3.Mp3AudioFile(path)
    tag = trackInfo.getTag()
    tag.link(path)
 
    print "Artist: %s" % tag.getArtist()
    print "Album: %s" % tag.getAlbum()
    print "Track: %s" % tag.getTitle()
    print "Track Length: %s" % trackInfo.getPlayTimeString()
    print "Release Year: %s" % tag.getYear()
This package does meet our arbitrary requirements. The only regrettable aspect of the package is its lack of official Windows support. We’ll reserve judgment until after we’ve tried out our third possibility though.

Ned Batchelder’s id3reader.py
This module is probably the easiest of the three to install since it’s just one file. All you need to do is download it and put the file into the site-packages or somewhere else on your Python path. The primary problem of this parser is that Batchelder no longer supports it. Let’s see if there’s an easy way to get the information that we need.

import id3reader
 
#----------------------------------------------------------------------
def getTags(path):
    """"""
    id3r = id3reader.Reader(path)
 
    print "Artist: %s" % id3r.getValue('performer')
    print "Album: %s" % id3r.getValue('album')
    print "Track: %s" % id3r.getValue('title')
    print "Release Year: %s" % id3r.getValue('year')


import pprint
from mutagen.easyid3 import EasyID3
print(EasyID3.valid_keays.keas())





dict_keys(['album', 'bpm', 'compilation', 'composer', 'copyright', 'encodedby', 'lyricist', 'length', 'media', 'mood', 'title', 'version', 'artist', 'albumartist', 'conductor', 'arranger', 'discnumber', 'organization', 'tracknumber', 'author', 'albumartistsort', 'albumsort', 'composersort', 'artistsort', 'titlesort', 'isrc', 'discsubtitle', 'language', 'genre', 'date', 'originaldate', 'performer:*', 'musicbrainz_trackid', 'website', 'replaygain_*_gain', 'replaygain_*_peak', 'musicbrainz_artistid', 'musicbrainz_albumid', 'musicbrainz_albumartistid', 'musicbrainz_trmid', 'musicip_puid', 'musicip_fingerprint', 'musicbrainz_albumstatus', 'musicbrainz_albumtype', 'releasecountry', 'musicbrainz_discid', 'asin', 'performer', 'barcode', 'catalognumber', 'musicbrainz_releasetrackid', 'musicbrainz_releasegroupid', 'musicbrainz_workid', 'acoustid_fingerprint', 'acoustid_id'])


# dict_keys(['TIT2', 'TPE1', 'TALB', 'TCON', 'APIC:attached picture', 'WXXX:MP3-META Front Cover URL'])
# dict_keys(['TIT2', 'TPE1', 'TALB', 'TCON', 'APIC:attached picture', 'WXXX:MP3-META Front Cover URL'])
























***