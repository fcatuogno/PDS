#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:49:22 2020

@author: fabian
"""

## Inicialización del Notebook del TP2

import numpy as np
import scipy.signal as signal
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from pandas import DataFrame
from IPython.display import HTML

N  = 1000 # muestras
fs = 1000 # Hz


# Insertar aquí el código para inicializar tu notebook
########################################################

nn = 10*N

VentBarlett = signal.windows.bartlett(N)
VentHann = signal.windows.hann(N)
VentBlack = signal.windows.blackman(N)
VentFlat = signal.windows.flattop(N)

plt.close('all')

fig, [ax1, ax2] = plt.subplots(1,2)
ax1.plot(VentBarlett, label='Barlett')
ax1.plot(VentHann, label='Hanning')
ax1.plot(VentBlack, label='Blackman')
ax1.plot(VentFlat, label='Flat-Top')
ax1.set_title('Forma de onda temporal Ventanas', fontsize = 'xx-large')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('N')
ax1.legend()  # Add a legend.

VentBarlett = np.concatenate((VentBarlett,np.zeros(nn)))
VentHann = np.concatenate((VentHann,np.zeros(nn)))
VentBlack = np.concatenate((VentBlack,np.zeros(nn)))
VentFlat = np.concatenate((VentFlat,np.zeros(nn)))

espectroBarlett = np.abs(np.fft.fft(VentBarlett))/len(VentBlack)
espectroHann = np.abs(np.fft.fft(VentHann))/len(VentBlack)
espectroBlack = np.abs(np.fft.fft(VentBlack))/len(VentBlack)
espectroFlat = np.abs(np.fft.fft(VentFlat))/len(VentBlack)
frec = np.fft.fftfreq(len(VentBlack),1/len(VentBlack))


ax2.plot(frec,np.log10(espectroBarlett), label='Barlett')
ax2.plot(frec,np.log10(espectroHann), label='Hanning')
ax2.plot(frec,np.log10(espectroBlack), label='Blackman')
ax2.plot(frec,np.log10(espectroFlat), label='Flat-Top')
plt.xlim(-100, 100)

ax2.yaxis.set_major_locator(MultipleLocator(1))
# ax2.yaxis.set_major_formatter(FormatStrFormatter('%d'))
# For the minor ticks, use no labels; default NullFormatter.
ax2.yaxisaxis.set_minor_locator(MultipleLocator(1))

ax2.set_title('Respuesta Frec Ventanas', fontsize = 'xx-large')
ax2.set_ylabel('Amplitud')
ax2.set_xlabel('K')

ax2.legend()



