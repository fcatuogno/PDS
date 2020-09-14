#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:23:08 2020

@author: fabian
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import MisFunciones as my

#%% Comienzo del ejemplo "#%%"

#####################################
# Uso de variables y tipos de datos #
#####################################

# flotantes, enteros o tipos numéricos
Fs = 1000.0 # Hz
N = 128 # muestras

A = 1.0
PHI = np.pi #rad
Offset = 0 #Volt
Frec = 100#Hertz

K=2
    #%% Generacion de Tono puro para utilizar en DFT

#Funcion con frecuencia multiple de frec spectral
# tiempo, seno = my.mi_funcion_sen( A, Offset, F=K*Fs/N, PHI, N, Fs)

#Funcion con frecuencia adrbitraria
tiempo, seno = my.mi_funcion_sen( A, Offset, Frec, PHI, N, Fs)


continua = 2*A*np.ones(len(tiempo))

senoidalcondc = seno + continua


mpl.pyplot.close('all')

# fig, [ax1, ax2, ax3] = plt.subplots(3, 1)

# ax1.stem(tiempo, seno, use_line_collection = True)   
# ax2.stem(tiempo, continua, use_line_collection = True)
# ax3.stem(tiempo, senoidalcondc, use_line_collection = True)

#Llamo a mi analizador sin pasarle Fs, ni normalizar amplitud:
my.mi_analizador(seno)
#Llamo a mi analizador sin pasarle Fs, pero normalizando amplitud
my.mi_analizador(seno, Normalizado = True)
#Llamo a mi analizador pasandole Fs, sin normalizando amplitud
my.mi_analizador(seno, Fs)
#Llamo a mi analizador pasandole Fs, y normalizando amplitud
my.mi_analizador(seno, Fs, True)


kk = np.arange(-N/2,N/2,1/Fs )
Dirichletkernel = np.sin(np.pi*kk) / np.sin(np.pi*kk/N)
# Dirichletkernel = np.sin(np.pi*K*kk)


fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
ax.plot(kk,Dirichletkernel)
