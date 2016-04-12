#!/usr/bin/env python

import os
import sys

def main():
    if not len(sys.argv) == 3:
        print 'Usage: {0} ACCELFILE OUTFILE.birds'.format(sys.argv[0])
        exit()

    accelfile = sys.argv[1]
    birdsfile = sys.argv[2]

    print 'Reading accelfile {0}'.format(accelfile)
    # read accelfile
    with open(accelfile, 'r') as infile:
        data = infile.readlines()
    # start at 4th line
    i = 3
    line = data[i].strip().split()
    birdsdata = []
    while not line == []:
        # Frequency without error
        freq = line[6].split('(')[0]
        # Number of harmonics
        numharm = line[4]
        birdsdata.append('{0}\t0.02\t{1}\t0\t0\n'.format(freq, numharm))
        i += 1
        line = data[i].strip().split()

    # Only first nmax birds
    nmax = 100
    if len(birdsdata) > nmax:
        birdsdata = birdsdata[:nmax]

    print 'Generating birds file {0}'.format(birdsfile)
    # write to birds file
    with open(birdsfile, 'w') as outfile:
        outfile.write('#Freq\tWidth\t#harm\tgrow?\tbary?\n')
        for line in birdsdata:
            outfile.write(line)


if __name__ == '__main__':
    main()
