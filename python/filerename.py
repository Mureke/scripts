import os
import sys
import shutil

def rename_files(dir):
    counter = 0
    for fname in os.listdir(dir):
        if '_' in fname:
            newFname = fname.split('_', 1)[1]
            newFname = newFname.split('.', 1)[0]
            mime = fname.split('.', 1)[1]
            print('Renaming file ' + fname + ' to ' + newFname + '.' + mime)
            shutil.move(dir + '/' +fname, dir + '/' + newFname + '.' + mime)
            counter += 1
    return counter

if(__name__ == '__main__'):
    if len(sys.argv) != 2:
        print('ERROR: Directory name not given!')
        sys.exit(1)
    dir = sys.argv[1]
    files = rename_files(dir)
    print('%i filenames changed' % files)
