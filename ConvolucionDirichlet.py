#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:39:04 2020

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

N  = 80 # muestras
fs = 100 # Hz

##################
# a.4) Senoidal #
#################

a0 = 1     # Volts
p0 = 0     # radianes
#f0 = fs+10 # Hz

Offset = 0 #Volt

K = 1 #Orden del Kernel (Ancho del Lobulo)
desfase = 10 #Desfase del Kernel respecto al anterior
A = 1 #Relacion de Amplitud del Kernel respecto al anterior

kk = np.arange(-N/2,N/2,1/fs )
Dirichletkernel = np.sin(1*np.pi*kk) / np.sin(1*np.pi*kk/N)

Dirichletkernel2 = A*np.sin(1/K*np.pi*(kk-desfase)) / np.sin(1/K*np.pi*(kk-desfase)/N)

mpl.pyplot.close('all')

fig, ax1 = plt.subplots()
    
ax1.plot(kk,Dirichletkernel, label = 'kernel 1')
ax1.plot(kk,Dirichletkernel2, label = 'kernel 2')
# ax1.plot(kk,20*np.log10(Dirichletkernel), label = 'kernel 1')
# ax1.plot(kk,20*np.log10(Dirichletkernel2), label = 'kernel 2')


ax1.set_title('Kernel de Dirichlet')
ax1.set_ylabel('Amp [dB]')
ax1.set_xlabel('K [k]')

# conv = np.convolve(Dirichletkernel, Dirichletkernel2, 'same')
conv = np.convolve(Dirichletkernel2, Dirichletkernel, 'same')
ax1.plot(kk,conv/len(conv), label = 'convolucion')

# ax1.plot(kk,Dirichletkernel+Dirichletkernel2, label = 'Suma')

# ax1.plot(kk,Dirichletkernel*Dirichletkernel2/25, label = 'Producto')


ax1.legend()


