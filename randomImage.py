import sys
import os
import shutil
import random

"""
Script to produce a random image.  Takes a directory as an argument and
chooses a random image from it.  Copies that image to same path with the
filename of random.jpg.
"""


"""
Returns a list of the image files in the source directory.
"""
def findImages(source):
    path = source
    files = os.listdir(path)
    images = []

    fileTypes = ['jpg', 'png', 'gif', 'jpeg', 'tiff', 'tff']

    for file in files:
        if file[-4] == '.':
            if file[-3:] in fileTypes:
                images.append(file)
        elif file[-5] == '.':
            if file[-4] in fileTypes:
                images.append(file)
    if len(images) <= 0:
        print "No image files in source directory."
        sys.exit(1)

    return images

def chooseImage(images):
    for img in images:
        if img == 'random.jpg':
            images.pop(images.index(img))
    return random.choice(images)

def main():
    args = sys.argv[1:]
    if not args:
        print "usage: [--sourcedir dir]"
        sys.exit(1)

    if args[0] == '--sourcedir':
        source = os.path.abspath(args[1])
        del args[0:2]
    
    if os.path.exists(source) == False:
        print 'Source directory not valid.  Did you enter it correctly?'
        sys.exit(1)
    else:
        images = findImages(source)
        image = chooseImage(images)
        
        print 'Copying.................'
##        shutil.copyfile((source + '/' + image), (source + '/' + 'random.jpg'))

        try:
            shutil.copyfile((source + '/' + image), (source + '/' + 'random.jpg'))
        except Error:
            print 'source file and destination are the same'
        except IOError:
            print 'destination location is not writable'

if __name__ == "__main__":
    main()
