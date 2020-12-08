#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:12:01 2020

@author: fabian
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Simular para los siguientes tamaños de señal
N = np.array([10, 50, 100, 250, 500, 1000, 5000], dtype=np.int)
# N = [50000]

realizaciones = 50

media = 0
varianza = 2

plt.close('all')

tus_resultados_per = []

for nn in N:
    
    muestras = np.random.normal(media, np.sqrt(varianza), (nn, realizaciones))
    
    espectro = np.abs(np.fft.fft(muestras, axis=0))
    Periodograma = (espectro**2)/nn
    Periodograma = np.fft.fftshift(Periodograma, axes=0)
    
    frec = np.fft.fftfreq(Periodograma.shape[0],1/nn) #Normalizo en bins
    frec = np.fft.fftshift(frec)    
 
    Pxmean = np.mean(Periodograma,axis=1)
    Pxvar = np.var(Periodograma,axis=1)
 
    plt.figure()
    
    plt.plot(frec,Periodograma)
    plt.plot(frec,Pxmean,'r*--')
    plt.plot(frec,Pxvar,'g+')
    plt.title('Periodograma N = %i' %nn )
    # plt.ylim(-50,0)
    plt.grid()
    
    tus_resultados_per.append([np.mean(Pxmean)-varianza,np.mean(Pxvar)])
    
