#! /usr/local/bin/python3


'''
lesson04 activity

Paths and File Processing
1.  Write a program which prints the full path for all files in the current
    directory, one per line
2.  Write a program which copies a file from a source, to a destination
    (without using shutil, or the OS copy command).
3.  Advanced: make it work for any size file: i.e. don’t read the entire
    contents of the file into memory at once.

This should work for any kind of file, so you need to open the files in binary
mode: open(filename, 'rb') (or 'wb' for writing). Note that for binary files,
you can’t use readline() – lines don’t have any meaning for binary files.

Test it with both text and binary files (maybe jpeg or something of
your chosing).
'''


from pathlib import Path


def print_file_paths():
    # print full path for all files in current working directory
    p = Path.cwd()
    for i in list(p.glob('*')):
        print(i)
    return


def file_copy():
    # copy a text file
    with open('logo.jpg', 'rb') as infile, open('logo_copy.jpg', 'wb') as outfile:
        outfile.write(infile.read())
    # copy a binary file
    with open('logo.jpg', 'rb') as infile, open('logo_copy.jpg', 'wb') as outfile:
        outfile.write(infile.read())
    return


if __name__ == "__main__":
    print_file_paths()
    file_copy()
