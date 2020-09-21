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

a0 = 0.5    # Volts
p0 = 0     # radianes
#f0 = fs+10 # Hz

Offset = 0.5 #Volt

#################

fd = 0.5

bits = [2, 4, 8, 16]

mpl.pyplot.close('all')

potenciasenial = []
potencia = []

tiempo, xx = my.mi_funcion_sen( a0, Offset, fs/100+fd, p0, N, fs)

# fig, ax1 = plt.subplots()

# # ax1.stem(frec, 20*np.log10(modulo), use_line_collection = True)
# ax1.plot(tiempo,4*xx)
# ax1.set_title('Espectro de la señal')
# ax1.set_ylabel('Modulo []')
# ax1.set_xlabel('Frec [K]')

# ax1.grid(True)


for nn in bits:
    
    digital = my.ADC(xx,fs,fs/10,nn)
    potencia.append([digital])
        
    fig, ax1 = plt.subplots()
    ax1.plot(tiempo,2**nn*xx)

    ax1.stem(tiempo[::10], digital, use_line_collection = True)
    # ax1.plot(digital)
    ax1.set_title('Espectro de la señal')
    ax1.set_ylabel('Modulo []')
    ax1.set_xlabel('Frec [K]')

    ax1.grid(True)