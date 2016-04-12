#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

def main():
    datafile = 'SinglePulses.hdf5'
    pulses = pd.read_hdf(datafile, 'pulses')
    events = pd.read_hdf(datafile, 'events')
    # Select based on DM, etc
    events = events[events.Pulse.isin(pulses.index)]

    fig, ax = plt.subplots()
    ax.autoscale(tight=True)
    ax.scatter(events.Time, events.DM, s=events.Sigma**2)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('DM (pc/cm$^3$)')
    ax.set_title('Events')
    plt.show()

if __name__ == '__main__':
    main()
