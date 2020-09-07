#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 01:46:31 2020

@author: fabian

TestBench para DFT() implementada en Tarea2
"""


import numpy as np


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


def DFTFrec(N,Fs):
    
    '''Retorna array de frecuencia desnormalizada para Fs.

    Keyword arguments:
    N -- Numero de muestras de la FFT
    Fs -- Frecuencia de Sampleo
                                

    Returns: array of float

    '''  
    
    frec = np.arange(0,N/2)
    frecneg = np.arange(-N/2,0)

    return (Fs/N)*np.concatenate([frec,frecneg])



