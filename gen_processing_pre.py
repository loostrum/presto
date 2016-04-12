#!/usr/bin/env python

import os

def gen_processing_commands(filename, outputname):
    '''
    Create process_pre.sh file with processing commands for given file.
    '''
    print 'Generating processing file for {0} and data file {1}'.format(outputname, filename)
    opts = {'fil':filename, 'out':outputname, 'numharm':8}
    template = '''# Processing commands for {out}
prepdata -nobary -o {out}_topo_DM0.00 -dm 0.0 -mask {out}_rfifind.mask -numout 500000 {fil}
realfft {out}_topo_DM0.00.dat
accelsearch -numharm {numharm} -zmax 0 {out}_topo_DM0.00.dat
/home/loostrum/sdb/scripts/gen_birds.py {out}_topo_DM0.00_ACCEL_0 {out}.birds
cp {out}_rfifind.inf {out}.inf
LD_LIBRARY_PATH=/home/joerivl/external/pgplot:$LD_LIBRARY_PATH
makezaplist.py {out}.birds
zapbirds -zap -zapfile {out}.zaplist {out}_topo_DM0.00.fft
DDplan.py -o ddplan.ps $(/home/loostrum/sdb/scripts/gen_ddplan_args.py {out}.inf) > ddplan.txt
cat ddplan.txt
'''

    with open('processing_pre.sh', 'w') as outfile:
        outfile.write(template.format(**opts))
    os.chmod('processing_pre.sh', 0755)


def main():
    defaultdir = '/projects/0/lotaas/data/loostrum/sdb/gbt/HE0532'
    defaultfile = '*.fits'
    datadir = raw_input('Datadir? {0}\n'.format(defaultdir))
    if datadir == '':
        datadir = defaultdir[:]
    datafile = raw_input('Datafile? {0}\n'.format(defaultfile))
    if datafile == '':
        datafile = defaultfile[:]
    defaultoutput = datafile.split('.')[0]
    outputname = raw_input('Output name? {0}\n'.format(defaultoutput))
    if outputname == '':
        outputname = defaultoutput[:]
    gen_processing_commands(os.path.join(datadir, datafile), outputname)

if __name__ == '__main__':
    main()
