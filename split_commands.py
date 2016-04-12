#!/usr/bin/env python

import sys
import os

import numpy as np

def main():
    if not len(sys.argv) == 3:
        print "Usage: split_commands.py FILENAME NOUT"
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print 'File not found: ', filename
    basename, ext = os.path.splitext(filename)

    try:
        nout = int(sys.argv[2])
    except ValueError:
        print 'Could not convert to int: ', sys.argv[2]
        sys.exit(1)

    cmds = np.loadtxt(filename, dtype=str)
    for i, cmdpart in enumerate(np.array_split(cmds, nout)):
        if i+1 < 10:
            name = '{0}_0{1}{2}'.format(basename, i+1, ext)
        else:
            name = '{0}_{1}{2}'.format(basename, i+1, ext)
        np.savetxt(name, cmdpart, fmt='%s')

if __name__ == '__main__':
    main()
