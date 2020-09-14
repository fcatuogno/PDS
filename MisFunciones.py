#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 01:46:31 2020

@author: fabian

TestBench para DFT() implementada en Tarea2
"""


import numpy as np
import matplotlib.pyplot as plt

#%% Separación de bloques de código para ordenar tu trabajo "#%%"
# Definición de funciones: saltear al comienzo del ejemplo, y volver cuando 
# se invoquen.

def mi_funcion_sen( vmax, dc, ff, ph, nn, fs):
    '''Genera una senial senoidal con los parametros indicados.

    Keyword arguments:
    vmax -- Valor pico de la senoidal
    dc -- componente de continua de la senial
    ff -- frecuencia de la senial
    ph -- fase de la senial
    nn -- numero de muestras de la senial
    fs - frecuencia de muestro de la senial
                                

    Returns: array of float, array of float

    '''  
    tt = np.arange(0.0, nn/fs, 1/fs)
    
    xx = dc + vmax*np.sin((2*np.pi*ff*tt+ph))
    
    return(tt, xx)
    

def DFT(x):
    '''Retorna Transformada de Fourier Discreta de la secuencia brindada.

    Keyword arguments:
    x -- Secuencia a la cual se le calcula la DFT
                                

    Returns: array of complex

    '''  
    
    N = len(x)
    
    X = np.zeros(N, complex)

    for m in np.arange(N):
        for n in np.arange(N):
            X[m] += np.complex(x[n])*np.exp(-2j*np.pi*n*m/N)
            
    
    return X


def DFTFrec(N,Fs = False):
    
    '''Retorna array de frecuencia desnormalizada para Fs.

    Keyword arguments:
    N -- Numero de muestras de la FFT
    Fs -- Frecuencia de Sampleo
                                

    Returns: array of float

    '''  
    ResEsp = {False: 1,
            True: Fs/N}
    frec = np.arange(0,N/2)
    frecneg = np.arange(-N/2,0)

    return (ResEsp[bool(Fs)])*np.concatenate([frec,frecneg])


#Pendiente: Agregar posibilidad de escalar, posibilidad de presentar en dB
def mi_analizador(xx, Fs = False, Normalizado = False) :
    
    '''Retorna modulo, fase y recuencia del espectro de la señal brindada.
         Grafica modulo y fase con frecuencia desnormalizada a Fs/2

    Keyword arguments:
    xx -- senial a analizar
    Fs -- Frecuencia de Sampleo, False para graficar en funcion de N. Default = false.
    Normalizado -- bool, si es True la frecuencia es normalizada por N. default = false.
                              

    Returns: array of float, array of float, array of float

    '''
    N = len(xx)
    
    if(not Fs):
        Fs = N
        
    #XX = DFT(xx)
    XX = np.fft.fft(xx) #Versión optimizada
    
    if(Normalizado):
        modulo, fase = np.abs(XX)/N, np.angle(XX, True)
    else:
        modulo, fase = np.abs(XX), np.angle(XX, True)
        
    frec = DFTFrec(N,Fs)
    
    fig, [ax1, ax2] = plt.subplots(2, 1, sharex=True)
    
    ax1.stem(frec, modulo, use_line_collection = True)
    ax1.set_title('Espectro de la señal')
    ax1.set_ylabel('Modulo')
    ax1.grid(True)

    
    ax2.stem(frec, fase, use_line_collection = True)
    ax2.set_ylim(-180, 180)
    ax2.set_xlim(-Fs/2, Fs/2)
    #ax2.set_title('Fase')
    ax2.set_xlabel('Frec [Hz]')
    ax2.set_ylabel('Fase [°]')
    ax2.grid(True)

    
    return modulo,fase,frec
