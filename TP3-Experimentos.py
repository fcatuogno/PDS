#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:50:56 2020

@author: fabian
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as signal

realizaciones = 100

#N = np.array([10, 50, 100, 250, 500, 1000, 5000], dtype=np.float)
N = 100

media = 0
varianza = 2

EspacioMuestral = np.random.normal(media,np.sqrt(varianza),(realizaciones,N))


plt.close('all')
plt.figure(1)
plt.plot(EspacioMuestral[50,:])
plt.plot(EspacioMuestral[:,10])

espectro = np.abs(np.fft.fft(EspacioMuestral, axis=0))
espectro = np.fft.fftshift(espectro, axes=0)
espectro *= (espectro/N)
frec = np.fft.fftfreq(espectro.shape[0],1/N)
frec = np.fft.fftshift(frec)  
espectro = 2*espectro[int(N/2):,:]
frec = frec[int(N/2):]

plt.figure(2)
plt.plot(frec,espectro)

plt.xlim(0,N/2)
plt.ylim(-2,40)

varianza = np.var(EspacioMuestral, axis = 0)
mediaxbin = np.mean(EspacioMuestral, axis = 1)