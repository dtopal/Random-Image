"""
Test handle for the random image generator.

Script should take in a given directory, choose a random image in that directory,
and copy it as random.img.

Things to test:
1) does it create random.img?
2) if random.img already exists, does it get replaced with a new file?
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
    

"""
Test 1 - Does it create random.img?
"""
def randomExist():
    if os.path.exists('./Test/random.img') == False:
        return False
    else:
        return True

def testCreateRandom():
    if os.name == 'nt':
        cmd = 'del .\\Test\\random.img'
    elif os.name == 'posix':
        cmd = 'rm ./Test/random.img'

    if randomExist() == True:
        print 'random.img already exists, removing....'
        os.system(cmd)

    os.system('randomImage.py --sourcedir ./Test/')

    if randomExist() == False:
        print 'FAILURE - random.img not created!'
        sys.exit(1)
    else:
        print 'OK - random.img created'





def main():
    checkFiles()
    testCreateRandom()


        
##        os.system('python ./randomImage.py')
        

if __name__ == '__main__':
    main()
