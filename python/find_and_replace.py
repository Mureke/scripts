import os, sys
from pprint import pprint
import subprocess


def replace(dir, word):
    command = 'find %s -type f -exec sed -i "s/%s/%s/g" {} \;' % (dir_path, word['Suomi'], word['Ruotsi'])
    print(command)
    subprocess.call([command], shell=True)


def execute(file, dir_path):
    word_list = []

    with open(file, mode='r') as input_file:
        rows = []
        for row in input_file:
            rows.append(row.rstrip('\n').split(";"))
        keys = rows[0]
        for value in rows[1:]:
            word_list.append(dict(zip(keys, value)))

    for word in word_list:
        replace(dir_path, word)

    return True


if __name__ == '__main__':
    file_path = sys.argv[1]
    dir_path = sys.argv[2]
    if file_path and dir_path:
        execute(file_path, dir_path)

