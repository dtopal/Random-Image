import sys
import os
import shutil
import random

"""
Script to produce a random image.  Takes a directory as an argument and
chooses a random image from it.  Copies that image to same path with the title
of random and the same suffix as the source file.
"""


"""
Returns a list of the image files in the source directory.
"""
def findImages(source):
    path = source
    files = os.listdir(path)
    images = []

    fileTypes = ['jpg', 'png', 'img', 'gif', 'jpeg', 'tiff', 'tff']

    for file in files:
        if file[-4] == '.':
            if file[-3:] in fileTypes:
                images.append(file)
        elif file[-5] == '.':
            if file[-4] in fileTypes:
                images.append(file)
        else:
            print "No image files in source directory."
            sys.exit(1)

    return images

def chooseImage(images):
    for img in images:
        if img == 'random.img':
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
##        if image[-4] == '.':
##            copyName = 'random.' + image[-3:]
##        elif image[-5] == '.':
##            copyName = 'random.' + image[-4:]
        print 'Copying.................'
        shutil.copyfile((source + '/' + image), (source + '/' + 'random.img'))
##        print source + '/' + copyname

if __name__ == "__main__":
    main()
