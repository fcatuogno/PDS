#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:23:05 2020

@author: fabian
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.signal as signal


#Resolucion espectral
############################

N  = 1000 # muestras
fs = 90 # Hz

##################
# a.4) Senoidal #
#################

#Desintonía
fd = [0.01, 0.25, 0.5]

#Tono 1
a1 = 1     # Volts
p1 = 0     # radianes
f1 = fs/4 # Hz

Offset = 0 #Volt
p0 = 0


#Tono 2
#a2_dB = np.linspace(-300,-100,10)   #Valores para pruebas sin leakage
a2_dB = np.linspace(-40,0,10)        #Valores para pruebas con leakage
# a2_dB = np.array([-40])
a2 = 10**(a2_dB/20)
f2 = f1 + 10*fs/N

######################################
#Generacion de matriz tiempo
######################################
t0 = np.zeros(len(a2))
tf = np.ones(len(a2))*(N-1)/fs

tt = np.linspace(t0, tf, N)
# tt = np.arange(0.0, N/fs, 1/fs)

######################################
#GEneracion de tonos
######################################

matriz2 = a2*np.sin((2*np.pi*f2*tt+p1))

#######################################
#Generacion de Ventanas
#######################################

# Ventanas = { 0:'Rectangular', 1:'Bartlett', 2:'Hanning', 3:'Blackman', 4:'Flattop' }
Ventanas = { 0:'Rectangular'}

# Generacion de Matriz con Ventanas
########################################################
VentRect = np.ones(N).reshape((N,1))
VentBarlett = signal.windows.bartlett(N).reshape((N,1))
VentHann = signal.windows.hann(N).reshape((N,1))
VentBlack = signal.windows.blackman(N).reshape((N,1))
VentFlat = signal.windows.flattop(N).reshape((N,1))

ventana = np.column_stack(([VentRect, VentBarlett,VentHann, VentBlack, VentFlat]))

##############################################
#Graficas temporales
############################################
plt.close('all')

# fig, ax1 = plt.subplots()

# for index in np.arange(len(a2)):
    
 #    ax1.plot(tt[0:,index],matriz[0:,index])

############################################
#Calculo de DFT
###########################################
for index in Ventanas:
    for f0 in fd:

        matriz = matriz2 + a1*np.sin((2*np.pi*(f1+f0*fs/N)*tt+p1))
    
        espectro = np.abs(np.fft.fft(matriz*ventana[0:,index].reshape(N,1), axis=0))*N
        espectro = np.fft.fftshift(espectro, axes=0)
        espectro = 20*np.log10(espectro)
        
        frec = np.fft.fftfreq(espectro.shape[0],0.5) #Normalizo respecto a Fs
        frec = np.fft.fftshift(frec)    
        
        fig, ax1 = plt.subplots()
            
        ax1.plot(frec,espectro)
        ax1.set_title('Ventana %s - fd = %f' %(Ventanas[index], f0), fontsize = 'xx-large')
        plt.xlim(0.4,0.6)    
        ax1.set_ylabel('Amplitud')
        ax1.set_xlabel('N')
        # a2_dB.astype('int32')
        ax1.legend(a2_dB.astype('int32'),loc='upper right', fontsize='x-large')  # Add a legend.
        plt.grid()
