#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:32:34 2020

@author: fabian
"""


import MisFunciones as my
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as signal

#Resolucion espectral - Realizaciones
############################

N  = 100 # muestras
fs = 90 # Hz

realizaciones = 200

##################
# a.4) Senoidal #
#################

a1 = 2     # Volts
p1 = 0     # radianes
f1 = fs/4 # Hz

Offset = 0

desintonia = np.random.uniform(-2,2,realizaciones)

#############################################
#Generación de matriz de realizaciones#
#############################################
matriz = np.ndarray((0,N))

for fr in desintonia:

    matriz = np.vstack((matriz,my.mi_funcion_sen( a1, Offset, f1+fr*fs/N, p1, N, fs)[1]))        
    
matriz = matriz.transpose()

