#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 23:28:17 2020

@author: fabian
"""

import numpy as np
import MisFunciones as my
import matplotlib as mpl
import matplotlib.pyplot as plt

N = 1024

ruido = my.GaussNoise(N,0,1)*3
ruido2 = my.GaussNoise(N,0,1.028)
ruido3 = my.GaussNoise(N,0,0.935)

tt = np.arange(0,1,1/N)


a = np.correlate(list(ruido),list(ruido), mode='full')
b = np.correlate(list(ruido2),list(ruido2), mode='full')
c = np.correlate(list(ruido3),list(ruido3), mode='full')

ffa=np.abs(np.fft.fft(a))
ffb=np.abs(np.fft.fft(b))
ffc=np.abs(np.fft.fft(c))

plt.close('all')

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(tt,ruido, label='μ=0 σ²=1')   # Plot some data on the axes.
ax.plot(tt,ruido2, label='μ=0 σ²=1.028')  # Plot some data on the axes.
ax.plot(tt,ruido3, label='μ=0 σ²=0.935')  # Plot some data on the axes.

ax.set_xlabel('Tiempo [segundos]')           # and here?
ax.set_ylabel('Amplitud [V]')          # and here?
ax.set_title('Señal: Ruido')   # and here?
ax.legend()  # Add a legend.
fig.show()

fig2, ax2 = plt.subplots()  # Create a figure containing a single axes.
ax2.plot(a/N, label='μ = 0 σ² = 1')   # Plot some data on the axes.
ax2.plot(b/N, label='μ=0 σ²=1.028')  # Plot some data on the axes.
ax2.plot(c/N, label='μ=0 σ²=0.935')  # Plot some data on the axes.

ax2.set_xlabel('')           # and here?
ax2.set_ylabel('')          # and here?
ax2.set_title('Autocorrelación')   # and here?
ax.legend()  # Add a legend.
fig.show()


fig3, ax3 = plt.subplots()  # Create a figure containing a single axes.
ax3.plot(ffa/N, label='μ = 0 σ² = 1')   # Plot some data on the axes.
ax3.plot(ffb/N, label='μ=0 σ²=1.028')  # Plot some data on the axes.
ax3.plot(ffc/N, label='μ=0 σ²=0.935')  # Plot some data on the axes.

ax3.set_xlabel('Frec')           # and here?
ax3.set_ylabel('Amp')          # and here?
ax3.set_title('Espectro Ruido')   # and here?
ax3.legend()  # Add a legend.
fig.show()