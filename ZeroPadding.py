#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:00:34 2020

@author: fabian
"""

import MisFunciones as my
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt



#%% Comienzo del ejemplo "#%%"

#####################################
# Uso de variables y tipos de datos #
#####################################

# NO modifiques este bloque
############################

N  = 1000 # muestras
fs = 1000 # Hz

##################
# a.4) Senoidal #
#################

a0 = 1     # Volts
p0 = 0     # radianes
#f0 = fs+10 # Hz

Offset = 0 #Volt


tus_resultados = []
                   
fd =  0.5

mpl.pyplot.close('all')

# tiempo, senial = my.mi_funcion_sen( a0, Offset, fs/4+fd, p0, N, fs)

#for f0 in fn:
f0 = 8
tiempo, xx = my.mi_funcion_sen( a0, Offset, f0*fs/N, p0, N, fs)
xx[:int(2*N/f0)] = 0
xx[int(3*N/f0):] = 0

f0 = 9
tiempo, xx2 = my.mi_funcion_sen( a0, Offset, f0*fs/N, p0, N, fs)
xx2[int(1*N/f0):] = 0

senial=xx+xx2


mj=[0, int(N/10), N, N*10]
# mj = [0]

for nn in mj:
    
    xx = np.concatenate((senial,np.zeros(nn)))
    
    ff = np.fft.fft(xx)
    modulo = np.abs(ff)/len(xx)
    frec = np.fft.fftfreq(len(xx),1/fs)
    # frec = np.fft.fftfreq(len(xx),1/len(xx))

    
    fig, [ax1,ax2] = plt.subplots(2,1)
    ax1.plot(xx)
    
    #fig, ax1 = plt.subplots()
    #ax1.stem(frec, 20*np.log10(modulo), use_line_collection = True)
    ax2.stem(frec, modulo, use_line_collection = True)
    ax2.set_title('Espectro de la señal')
    ax2.set_ylabel('Modulo []')
    ax2.set_xlabel('Frec [Hz]')
    plt.xlim(0, 260)
    

    ax1.grid(True)
    
    
    deltaf = fs/len(xx)
    print(deltaf)
    f0 = np.argmax(modulo[:int(len(xx)/2)])
    f0 = frec[int(f0)]
    print(f0)

    tus_resultados.append([f0, np.around(100*((fs/4+fd)-f0)/(fs/4+fd),2)]) 
    # if(len(tus_resultados)):
    #     tus_resultados.append([f0, np.around(100*(f0-tus_resultados[0][0])/tus_resultados[0][0],2)])
    # else:
    #     tus_resultados.append([f0, 0])

    