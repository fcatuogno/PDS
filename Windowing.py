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

#Resolucion espectral
N  = 1000 # muestras
fs = 1000 # Hz

#ZeroPadding
nn = 10*N


Ventanas = { 0:'Rectangular', 1:'Bartlett', 2:'Hanning', 3:'Blackman', 4:'Flattop' }

# Generacion de Matriz con Ventanas
########################################################
VentRect = np.ones(N)
VentBarlett = signal.windows.bartlett(N)
VentHann = signal.windows.hann(N)
VentBlack = signal.windows.blackman(N)
VentFlat = signal.windows.flattop(N)

matriz = np.column_stack(([VentRect, VentBarlett,VentHann, VentBlack, VentFlat]))


#Graficas Temporales de Ventanas
plt.close('all')
fig, [ax1, ax2] = plt.subplots(1,2)

for index in Ventanas:
    
    ax1.plot(matriz[0:,index], label=Ventanas[index])
  

ax1.set_title('Forma de onda temporal Ventanas', fontsize = 'xx-large')
ax1.set_ylabel('Amplitud')
ax1.set_xlabel('N')
ax1.legend(loc='upper right', fontsize='large')  # Add a legend.

#Zero Padding
matriz = np.concatenate((matriz,np.zeros([nn, matriz.shape[1]])))

#Claculo de DFT
espectro = np.abs(np.fft.fft(matriz, axis=0))/len(VentBlack)
frec = np.fft.fftfreq(espectro.shape[0],1/fs)


#Graficas de Espectro
for index in Ventanas:
    
    ax2.plot(frec, np.log10(espectro[0:,index]), label=Ventanas[index])
 
plt.xlim(-10, 10)
plt.ylim(-12,0)
ax2.set_title('Respuesta Frec Ventanas', fontsize = 'xx-large')
ax2.set_ylabel('Amplitud')
ax2.set_xlabel('Frec [Hz]')
ax2.legend(loc='lower right', fontsize='large')
