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

Ventanas = { 0:'Rectangular', 1:'Bartlett', 2:'Hanning', 3:'Blackman', 4:'Flattop' }

# Generacion de Matriz con Ventanas
########################################################
VentRect = np.ones(N).reshape((N,1))
VentBarlett = signal.windows.bartlett(N).reshape((N,1))
VentHann = signal.windows.hann(N).reshape((N,1))
VentBlack = signal.windows.blackman(N).reshape((N,1))
VentFlat = signal.windows.flattop(N).reshape((N,1))

ventana = np.column_stack(([VentRect, VentBarlett,VentHann, VentBlack, VentFlat]))

##################
# a.4) Senoidal #
#################

a1 = 2     # Volts
p1 = 0     # radianes
f0 = fs/4 # Hz

Offset = 0

desintonia = np.random.uniform(-2,2,realizaciones)
f1 = f0+desintonia*fs/N

bins_int = 2
##############################################
#Generacion de vector temporal
##############################################

t0 = np.zeros(realizaciones)
tf = np.ones(realizaciones)*(N-1)/fs

tt = np.linspace(t0, tf, N)

#############################################
#Generación de matriz de realizaciones#
#############################################

matriz = a1*np.sin((2*np.pi*f1*tt+p1))

##############################################
#Graficas Temporales de Ventanas
##############################################
plt.close('all')
# fig, ax1 = plt.subplots()

# for index in np.arange(realizaciones):
    
#     ax1.plot(matriz[0:,index])
  

# ax1.set_title('Forma de onda temporal', fontsize = 'xx-large')
# ax1.set_ylabel('Amplitud')
# ax1.set_xlabel('N')


##############################################
#Calculo de DFT aplicando la i-esima ventana
##############################################

sesgo = []
varianza = []

plt.figure(1)
for index in Ventanas:
    
    espectro = np.abs(np.fft.fft(matriz*ventana[0:,index].reshape(N,1), axis=0))*a1/N
    espectro = np.fft.fftshift(espectro, axes=0)
    frec = np.fft.fftfreq(espectro.shape[0],0.5) #Normalizo respecto a Fs
    frec = np.fft.fftshift(frec)    

    #Estimador - CASO 1
    # a0 = espectro[25,0:]
    
    #Estimador - CASO 2
    a0 = espectro[25-bins_int:25+bins_int+1,0:]
    a0 = (np.sqrt(np.sum(a0**2,axis=0)/5))
    
    
    fig, ax1 = plt.subplots()
    ax1.plot(f1,a0, 'x')
    
    
    sesgo.append(np.mean(a0)-a1)
    a_0_u = a0 - sesgo[index] 
    varianza.append(np.var(a0))
    ax1.set_title('%s' %Ventanas[index], fontsize = 'xx-large')
    plt.ylim(0, a1+0.1)

    plt.figure(1)
    # plt.hist(a0, 10, label = Ventanas[index])
    plt.hist(a_0_u, 10, label = Ventanas[index])  #Histograma con sesgo nulo

    plt.title('Histograma estimador  $ \hat{a_0} $', fontsize = 'xx-large')
    plt.ylabel('Cantidad de realizaciones', fontsize='x-large')
    plt.xlabel('Valor del estimador', fontsize='x-large')
    plt.legend(loc='upper right', fontsize='x-large')
  


    # fig, ax1 = plt.subplots()
        
    # for nn in np.arange(realizaciones):
    #     ax1.plot(frec,espectro[0:,nn], label=ventana[index])
        
    # ax1.set_title('Espectro N realizaciones %s' %Ventanas[index], fontsize = 'xx-large')

# ax1.set_ylabel('Amplitud')
# ax1.set_xlabel('N')


