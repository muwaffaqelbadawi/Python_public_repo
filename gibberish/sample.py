import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

fileHandler = logging.FileHandler('pepole.log')
fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

class person(object):
  def __init__(self, firstname, lastname):
    self.firstName = firstname
    self.lastName = lastname

    logger.info('my name is {0} - my email is {1}'.format(self.fullName, self.email))
  
  @property
  def email(self):
    return '{0}.{1}@email.com'.format(self.firstName, self.lastName)
  @property
  def fullName(self):
    return '{0} {1}'.format(self.firstName, self.lastName)

p1 = person('Carl', 'anderson')
p2 = person('Suzanne', 'Clark')
p3 = person('John', 'Doe')







# import os, math
# # from pygame import mixer
# from datetime import datetime
# from mutagen.id3 import ID3, TIT2
# from mutagen.mp3 import MP3

# path = ("C://Users//Muwaffuq//Music//Ariana Grande - imagine(MP3_128K).mp3")
# audioID3 = ID3(path)
# audioMP3 = MP3(path) 

# title = audioID3['TIT2'].text[0]
# artist = audioID3['TPE1'].text[0]
# album = audioID3['TALB'].text[0]
# genre = audioID3['TCON'].text[0]
# albumArtPicUrl = audioID3['WXXX:MP3-META Front Cover URL']
# albumArt = audioID3['APIC:attached picture']
# size = round(os.stat(path).st_size/1048576, 2)
# sort_by_modification_time = datetime.fromtimestamp( sort_by_modification_time )
#################################################################################
# title = audioMP3["TIT2"].text[0]
# artist = audioMP3['TPE1'].text[0]
# album = audioMP3['TALB'].text[0]
# genre = audioMP3['TCON'].text[0]
# composer = audioMP3['TCOM'].text[0]
# audioMP3['TSSE']
# length = audioMP3.info.length # in sec
# bitrate = audioMP3.info.bitrate/1000
# albumArtPicUrl = audioMP3['WXXX:MP3-META Front Cover URL']
# albumArt = audioMP3['APIC:attached picture']
# songPath = audioMP3.filename
################################################
# audioID3.getall('TSOP')
# audioID3.getall('TIT2')
# audioID3.getall('TTTT')
# lyrics = audioID3.getall("TEXT")
################################################
# year = audioID3.get("TYER")
################################################
# audioID3.add(TIT2(encoding=3, text=u"An example"))
# audioID3.save()
################################################
# album = audioEasyID3['album']
# audioEasyID3['copyright']
# time = audioEasyID3['date'] actual date
################################################
# time = datetime.fromtimestamp(length)
################################################
# mixer.init()
# mixer.music.load()
# mixer.music.play()
# mixer.sound()
################################################
# splitText = os.path.splitext(path)
# os.path.basename()
################################################
# divided total length/60 - mod - total length%60
# mins,secs =  divmod(length, 60)
# round(mins)
# round(secs)


# print("Artist: {}".format(artist))
# print("Artist: {}".format(artist.))
# print("Length: {}".format(length))
# print("Bitrate: {}".format(bitrate))

# print(audioMP3._Info(fileobj))
# print(audioMP3.pprint)
# print(audioID3.keys())
# print(audioMP3.keys())


# print(audioEasyID3['date'])
# print(  )