#!/usr/bin/env python

import os
import sys

def main():
    if not len(sys.argv) == 2:
        print 'Usage: {0} filename.inf'.format(sys.argv[0])
        exit()

    filename = sys.argv[1]
    outdata = {}
    # read file
    with open(filename, 'r') as infile:
        data = infile.readlines()
    for line in data:
        line = line.strip().split('=')
        line = [item.strip() for item in line]
        if len(line) == 2:
            outdata[line[0]] = line[1]
    # save / calc relevant params
    dmhigh = 500
    bandwidth = float(outdata['Total bandwidth (Mhz)'])
    fcentr = int(outdata['Number of channels']) / 2 * float(outdata['Channel bandwidth (Mhz)']) + float(outdata['Central freq of low channel (Mhz)']) - .5 * float(outdata['Channel bandwidth (Mhz)'])
    dt = float(outdata['Width of each time series bin (sec)'])
    nchan = int(outdata['Number of channels'])
    nsub = 114
    print '-n {0} -s {1} -l 0 -d {2} -t {3:.6f} -b {4} -f {5}'.format(nchan, nsub, dmhigh, dt, bandwidth, fcentr)

if __name__ == '__main__':
    main()
