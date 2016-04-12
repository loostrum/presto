#!/usr/bin/env python

import os
import sys

def main():
    if not len(sys.argv) in [2, 4, 5]:
        print 'Usage: {0} filename.inf (dmhigh nsub) or (dmlow dmhigh nsub)'.format(sys.argv[0])
        exit()

    filename = sys.argv[1]
    if len(sys.argv) == 4 :
        dmhigh = sys.argv[2]
        nsub = sys.argv[3]
    elif len(sys.argv) == 5:
        dmlow = sys.argv[2]
        dmhigh = sys.argv[3]
        nsub = sys.argv[4]
    else:
        dmlow = 0
        dmhigh = 500
        nsub = 114
    outdata = {}
    # read file
    with open(filename, 'r') as infile:
        data = infile.readlines()
    for line in data:
        line = line.strip().split('=')
        line = [item.strip().lower() for item in line]
        if len(line) == 2:
            outdata[line[0]] = line[1]
    # save / calc relevant params
    bandwidth = float(outdata['Total bandwidth (Mhz)'.lower()])
    fcentr = int(outdata['Number of channels'.lower()]) / 2 * float(outdata['Channel bandwidth (Mhz)'.lower()]) + float(outdata['Central freq of low channel (Mhz)'.lower()]) - .5 * float(outdata['Channel bandwidth (Mhz)'.lower()])
    dt = float(outdata['Width of each time series bin (sec)'.lower()])
    nchan = int(outdata['Number of channels'.lower()])
    print '-n {0} -s {1} -l {2} -d {3} -t {4:.6f} -b {5} -f {6}'.format(nchan, nsub, dmlow, dmhigh, dt, bandwidth, fcentr)

if __name__ == '__main__':
    main()
