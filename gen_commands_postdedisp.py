#!/usr/bin/env python

import os
import glob

def gen_processing_commands(filenames, outputname, baryv):
    '''
    Create process_post.sh file with processing commands for given file.
    '''

    print 'Generating processing file for {0}'.format(outputname)
    opts = {'out':outputname, 'baryv':baryv}
    template = 'realfft {fil}.dat; zapbirds -zap -zapfil {out}.zaplist -baryv {baryv} {fil}.fft; accelsearch -zmax 0 {fil}.dat'

    with open('processing_post.sh', 'w') as outfile:
        for fil in filenames:
            opts['fil'] = fil
            outfile.write(template.format(**opts))
    os.chmod('processing_post.sh', 0755)


def main():
    defaultoutput = '11100335'
    outputname = raw_input('Output name? {0}\n'.format(defaultoutput))
    if outputname == '':
        outputname = defaultoutput[:]
    baryv = "`cat baryv.txt`"
    filenames = glob.glob('{0}_DM*.dat'.format(outputname))
    filenames = [os.path.splitext(name)[0] for name in filenames]

    gen_processing_commands(filenames, outputname, baryv)

if __name__ == '__main__':
    main()
