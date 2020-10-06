#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 23:40:14 2020

@author: fabian
"""


import MisFunciones as my
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# NO modifiques este bloque
############################

N  = 1000 # muestras
fs = 1000 # Hz

##################
# a.4) Senoidal #
#################

a0 = np.sqrt(2)    # Volts
p0 = 0     # radianes
#f0 = fs+10 # Hz

Offset = 0 #Volt

#################

tus_resultados = [ ['$\sum_{f=0}^{f_S/2} \lvert S_R(f) \rvert ^2$', '$\sum_{f=0}^{f_S/2} \lvert S_Q(f) \rvert ^2$', '$\sum_{f=0}^{f_S/2} \lvert e(f) \rvert ^2$' ], 
                   ['',                                             '',                                             ''                              ], 
                   #['', '', ''], # <-- completar acá
                   #['', '', ''], # <-- completar acá
                   #['', '', ''], # <-- completar acá
                 ]

fd = 0

bits = [4, 8, 16]

mpl.pyplot.close('all')

potencia = []
e = []
hist = []

tiempo, xx = my.mi_funcion_sen( a0, Offset, fs/100+fd, p0, N, fs)
ruido = my.GaussNoise(len(xx),0,0.1)
#ruido = np.random.normal(0,1,N)

corr = np.correlate(ruido,ruido, mode='same')
potenciaruido = corr[int(N/2)]/len(corr)
potencia = np.mean(xx**2)
print(potencia)
print(potenciaruido)

xx += ruido
potencia = np.mean(xx**2)


################################################
##  Adecuacion de la señal para el ADC
################################################
continua = 0.5

xx /= 2*np.max(xx)
xx += continua

# fig, ax1 = plt.subplots()

# # ax1.stem(frec, 20*np.log10(modulo), use_line_collection = True)
# ax1.plot(tiempo,4*xx)
# ax1.set_title('Espectro de la señal')
# ax1.set_ylabel('Modulo []')
# ax1.set_xlabel('Frec [K]')

# ax1.grid(True)


for nn in bits:
    
    digital = my.ADC(xx,fs,fs/10,nn)
    
    e = (2**nn-1)*xx[::10] - digital
    hist.append(np.histogram(e,10))
    
    a = np.correlate(list(e),list(e), mode='full')
 
    fig, ax1 = plt.subplots()
    ax1.plot(tiempo,(2**nn-1)*xx,'g',label='analogica')
    ax1.plot(tiempo[::10],e,'r',label='error-ruido Q')

    ax1.stem(tiempo[::10], digital,label='digital', use_line_collection = True)
    # ax1.plot(tiempo[::10], digital,label='digital')
    ax1.set_title('Señal Analogica Vs Digital - Ruido Q', fontsize = 'xx-large')
    ax1.set_ylabel('Modulo []')
    ax1.set_xlabel('Frec [K]')
    
    ax1.grid(True)
    ax1.legend(loc='upper right', fontsize = 'xx-large')  # Add a legend.

    fig2, ax2 = plt.subplots()

    ax2.plot(a,label='error-ruido Q')
    ax2.set_title('Autocorrelacion ruido de cuatizacion', fontsize = 'xx-large')
    ax2.set_ylabel('Modulo []')
    ax2.set_xlabel('Frec [K]')
    
    fig, ax =  plt.subplots()
    plt.hist(a, bins='auto')  # arguments are passed to np.histogram
    
    tus_resultados.append([str(potencia), str(np.mean(digital**2)/(2**nn-1)**2), str(np.mean(e**2))])