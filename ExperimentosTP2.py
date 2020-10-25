#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:23:05 2020

@author: fabian
"""

import MisFunciones as my
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as signal


#Resolucion espectral
############################

N  = 100 # muestras
fs = 90 # Hz

##################
# a.4) Senoidal #
#################

a1 = 1     # Volts
p1 = 0     # radianes
f1 = fs/4 # Hz

a2_dB = -40

a2 = 10**(a2_dB/20)
f2 = f1 + 10*fs/N

Offset = 0 #Volt
p0 = 0


tus_resultados = []
plt.close('all')
fig, [ax1, ax2] = plt.subplots(1,2)

                   
fd = [0.5]

VentBarlett = signal.windows.bartlett(N)
VentHann = signal.windows.hann(N)
VentBlack = signal.windows.blackman(N)
VentFlat = signal.windows.flattop(N)


for f0 in fd:
    f1 = fs/4 + f0*fs/N
    f2 = f1 + 10*fs/N
        
    tiempo, xx = my.mi_funcion_sen( a1, Offset, f1, p0, N, fs)
    tiempo2, xx2 = my.mi_funcion_sen( a2, Offset, f2, p0, N, fs)
    xx += xx2
    xx_Barlett = xx*VentBarlett
    
    espectro = np.abs(np.fft.fft(xx))/len(xx)
    espectro = 20*np.log10(espectro)
    
    espectro_Barlett = np.abs(np.fft.fft(xx_Barlett))/len(xx)
    espectro_Barlett = 20*np.log10(espectro_Barlett)                                
    
    frec = np.fft.fftfreq(len(xx),1/N)
      
    ax1.plot(tiempo, xx, label='')
    ax1.plot(tiempo, xx_Barlett, label='')

    ax2.plot(frec,espectro, label='')
    ax2.plot(frec,espectro_Barlett, label='')
    
    ax1.set_title('Forma de onda temporal señal bitonal', fontsize = 'xx-large')
    ax1.set_ylabel('Amplitud')
    ax1.set_xlabel('Tiempo [s]')
    
    ax2.set_title('Espectro Señal bitonal', fontsize = 'xx-large')
    ax2.set_ylabel('Amplitud')
    ax2.set_xlabel('Frec [rad]')
    #plt.xlim(0, 0.157)
    
    
    ax1.legend()  # Add a legend.

