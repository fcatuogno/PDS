#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:34:29 2020

@author: fabian
"""

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
N = 1000
K = np.array([2, 5, 10, 20, 50], dtype=np.int)


realizaciones = 50

media = 0
varianza = 2

plt.close('all')

tus_resultados_per = []

muestra = np.random.normal(media, np.sqrt(varianza), (N, realizaciones))


for kk in K:
    ll = N//kk
    muestras = muestra.reshape(ll,kk*realizaciones,order='F')/kk
    
    espectro = np.abs(np.fft.fft(muestras, axis=0))
    Periodograma = (espectro**2)/ll
    Periodograma = np.fft.fftshift(Periodograma, axes=0)
    
    frec = np.fft.fftfreq(Periodograma.shape[0],1/ll) #Normalizo en bins
    frec = np.fft.fftshift(frec)    
 
    Pxmean = np.mean(Periodograma,axis=1)
    Pxvar = np.var(Periodograma,axis=1)
 
    plt.figure()
    
    plt.plot(frec,Periodograma,lw=0.4)
    plt.plot(frec,Pxmean,'r*--', lw=2)
    plt.plot(frec,Pxvar,'g*',lw=4)
    plt.title('Periodograma N = %i, K=%i' %(N,kk) )
    plt.xlim(0,ll//2)
    plt.grid()
    
    tus_resultados_per.append([np.mean(Pxmean-varianza),np.mean(Pxvar)])