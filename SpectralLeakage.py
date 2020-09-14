#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:43:21 2020

@author: fabian

Spectral Leakage
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


tus_resultados = [ ['$ \lvert X(f_0) \lvert$', '$ \lvert X(f_0+1) \lvert $', '$\sum_{i=F} \lvert X(f_i) \lvert ^2 $'], 
                   ['',                        '',                           '$F:f \neq f_0$']
                   ]
fd = [0.01, 0.25, 0.5]

mpl.pyplot.close('all')

for f0 in fd:
    tiempo, xx = my.mi_funcion_sen( a0, Offset, fs/4+f0, p0, N, fs)
    
    ff = np.fft.fft(xx)
    modulo = np.abs(ff)/N
    frec = np.fft.fftfreq(N,1/N)
    
    fig, ax1 = plt.subplots()
    
    # ax1.stem(frec, 20*np.log10(modulo), use_line_collection = True)
    ax1.stem(frec, modulo, use_line_collection = True)
    ax1.set_title('Espectro de la señal')
    ax1.set_ylabel('Modulo [dB]')
    ax1.set_xlabel('Frec [K]')

    ax1.grid(True)
    
    #modulo,fase,frec = my.mi_analizador(xx, N)
    
    potencia = (np.sum(modulo))**2
    
    tus_resultados.append([str(2*modulo[250]), str(2*modulo[251]), str(potencia-(2*modulo[250])**2)])
    
    tus_resultados2 = [ ['$ \lvert X(f_0) \lvert$', '$ \lvert X(f_0+1) \lvert $', '$\sum_{i=F} \lvert X(f_i) \lvert ^2 $'], 
                    ['',                        '',                           '$F:f \neq f_0$'], 
                  ['', '', ''], # <-- acá debería haber numeritos :)
                  ['', '', ''], # <-- acá debería haber numeritos :)
                  ['', '', ''], # <-- acá debería haber numeritos :)
                  ['', '', '']  # <-- acá debería haber numeritos :)
                  ]
    
    
