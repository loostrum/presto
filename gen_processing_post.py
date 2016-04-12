#!/usr/bin/env python

import os
import glob

import numpy as np

def gen_processing_commands(filenames, outputname, baryv, zmax):
    '''
    Create process_post.sh file with processing commands for given file.
    '''

    print 'Generating processing file for {0}'.format(outputname)
    opts = {'out':outputname, 'baryv':baryv, 'zmax':zmax}
    template = '; zapbirds -zap -zapfile {out}.zaplist -baryv {baryv} {fil}.fft'

    # split filenames into chunks of nmax for realfft (can do max 16 at once)
    nmax = 8
    chunks = np.array_split(filenames, len(filenames)//nmax + 1)
    with open('processing_post.sh', 'w') as outfile:
        for chunk in chunks:
            outfile.write('realfft -mem')
            for filename in chunk:
                outfile.write(' {0}.dat'.format(filename))
            for filename in chunk:
                opts['fil'] = filename
                outfile.write(template.format(**opts))
            outfile.write('\n')
    os.chmod('processing_post.sh', 0755)


def main():
    defaultoutput = os.getcwd().split('/')[-1]
    outputname = raw_input('Output name? {0}\n'.format(defaultoutput))
    if outputname == '':
        outputname = defaultoutput[:]
    with open('baryv', 'r') as infile:
        baryv = infile.readlines()
    baryv = float(baryv[0].strip())
    zmax = 100
    filenames = glob.glob('{0}_DM*.dat'.format(outputname))
    if len(filenames) == 0:
        print 'No .dat files found'
        exit()
    filenames = [os.path.splitext(name)[0] for name in filenames]
    filenames.sort(key=lambda name: float(name.split('{0}_DM'.format(outputname))[-1]))

    gen_processing_commands(filenames, outputname, baryv, zmax)

if __name__ == '__main__':
    main()
