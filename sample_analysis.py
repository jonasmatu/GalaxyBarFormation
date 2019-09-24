import numpy as np
import matplotlib.pyplot as plt
import tool_analyze as ta

# get data
from prepare_data import *


def bin_type(names):
    """Count the number of galaxies of a Hubble type in bins for
    E, S0, Sa, Sb, Sc, Sd
    Args:
        names (list): names of the galaxies.
    Returns:
        np.array: bins of types.
    """
    bins = np.zeros(6)
    hTypes = ta.get_type(names)
    for i in range(len(names)):
        if hTypes[i][0] == 'E':
            bins[0] += 1
        elif hTypes[i][1] == '0':
            bins[1] += 1
        elif hTypes[i][1] == 'a':
            bins[2] += 1
        elif hTypes[i][1] == 'b':
            bins[3] += 1
        elif hTypes[i][1] == 'c':
            bins[4] += 1
        elif hTypes[i][1] == 'd':
            bins[5] += 1
    return bins


def bin_mass(names):
    """Count the number of galaxies in a stellar mass range.
    9, 9.5, 10, 10.5, 11, 11.5
    Args:
        names (list)
    Returns:
        np.array: bins of mass"""
    M = ta.read_stellar_mass(names)
    bins = np.zeros(6)
    for i in range(len(names)):
        if M[i] < 9.25:
            bins[0] += 1
        elif M[i] < 9.75:
            bins[1] += 1
        elif M[i] < 10.25:
            bins[2] += 1
        elif M[i] < 10.75:
            bins[3] += 1
        elif M[i] < 11.25:
            bins[4] += 1
        else:
            bins[5] += 1
    return bins


def bin_redshift(names):
    """Bin the redshift"""
    z = ta.get_redshift(names)*1e2
    bins = np.zeros(6)
    for i in range(len(names)):
        if z[i] < 0.75:
            bins[0] += 1
        elif z[i] < 1.25:
            bins[1] += 1
        elif z[i] < 1.75:
            bins[2] += 1
        elif z[i] < 2.25:
            bins[3] += 1
        elif z[i] < 2.75:
            bins[4] += 1
        else:
            bins[5] += 1
    return bins


def plot_overview():
    sTypes = ['E', 'S0', 'Sa', 'Sb', 'Sc', 'Sd']
    nTypes = bin_type(names)
    fig, ax = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
    fig.subplots_adjust(wspace=0)
    ax[0].bar(sTypes, nTypes)
    ax[0].set_ylabel('Number')
    ax[0].set_title('Hubble Type')
    sMass = ['9', '9.5', '10', '10.5', '11', '11.5']
    nMass = bin_mass(names)
    ax[1].bar(sMass, nMass)
    ax[1].set_title(r'log(M/M$_\odot$)')
    sRedshift = ['0.5', '1', '1.5', '2', '2.5', '3']
    nRedshift = bin_redshift(names)
    ax[2].bar(sRedshift, nRedshift)
    ax[2].set_title(r'Redshift (x10$^{-2}$)')
    plt.show()
    plt.close()


if __name__ == "__main__":
    plot_overview()