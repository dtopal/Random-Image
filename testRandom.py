"""
Test handle for the random image generator.

Script should take in a given directory, choose a random image in that directory,
and copy it as random.jpg.

Things to test:
1) does it create random.jpg?
2) if random.jpg already exists, does it get replaced with a new file?
"""

import os
import sys


"""
Are all the relevant files present?
"""
def checkFiles():
    if os.path.exists('./randomImage.py') == False:
        print 'random.py... NOT PRESENT'
        sys.exit(1)
    else:
        print 'random.py... PRESENT'

    if os.path.exists('./Test/') == False:
        print '/Test/ .... NOT PRESENT'
        sys.exit(1)
    else:
        print '/TEST/ .... PRESENT'

    if os.listdir('./Test/') == False:
        print 'Test images.......  NOT PRESENT'
        sys.exit(1)
    else:
        print 'Test images........ PRESENT'

    
def randomExist():
    if os.path.exists('./Test/random.jpg') == False:
        return False
    else:
        return True


"""
Test 1 - Does it create random.jpg?
"""
def testCreateRandom():
    if os.name == 'nt':                     ##Quick OS check
        cmd = 'del .\\Test\\random.jpg'
    elif os.name == 'posix':
        cmd = 'rm ./Test/random.jpg'

    if randomExist() == True:
        print 'random.img already exists, removing....'
        os.system(cmd)

    try:
        os.system('python randomImage.py --sourcedir ./Test/')
    except Error:
        print 'source file and destination are the same'
    except IOError:
        print 'destination location is not writable'
        

    if randomExist() == False:
        print 'FAILURE - random.jpg not created!'
        sys.exit(1)
    if randomExist() == True:
        print 'OK - random.jpg created'





def main():
    checkFiles()
    testCreateRandom()


        
##        os.system('python ./randomImage.py')
        

if __name__ == '__main__':
    main()
