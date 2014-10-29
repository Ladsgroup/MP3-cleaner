import fnmatch
import os
import eyed3
import shutil
path_to_clean = u'/media/amir/Files/Download/'
path_to_move = u'/media/amir/Files/Music/'
matches = []
for root, dirnames, filenames in os.walk(path_to_clean):
    for filename in fnmatch.filter(filenames, u'*.mp3'):
        matches.append(os.path.join(root, filename))
print len(matches)
for file in matches:
    file = eval("u\"%s\"" % file)
    try:
        audiofile = eyed3.load(file)
        artist = audiofile.tag.artist
        album = audiofile.tag.album
        try:
            os.mkdir('%s%s' % (path_to_move, artist))
        except OSError:
            pass
        try:
            os.mkdir('%s%s/%s' % (path_to_move, artist, album))
        except OSError:
            shutil.move(file, u'%s%s/%s/%s' % (path_to_move, artist, album, file.split("/")[-1]))
            print "moved"
        except:
            print "Not moved"
            pass
        else:
            shutil.move(file, u'%s%s/%s/%s' % (path_to_move, artist, album, file.split("/")[-1]))
            print "Moved"
    except:
        pass
