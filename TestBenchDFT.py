# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
import MisFunciones as my

#%% Comienzo del ejemplo "#%%"

#####################################
# Uso de variables y tipos de datos #
#####################################

# flotantes, enteros o tipos numéricos
Fs = 50.0 # Hz
N = 256 # muestras

A = 1.0
PHI = np.pi #rad
Offset = 0 #Volt
Frec = 4#Hertz

    #%% Generacion de Tono puro para utilizar en DFT

tiempo, tension = my.mi_funcion_sen( A, Offset, Frec, PHI, N, Fs)

    #%% LLamados a Transformadas de Fourier

#Llamado a funcion que realiza DFT y que genera vector de frecuencia desnormalizado
startDFT = time.time()
X = my.DFT(tension)
endDFT=time.time()

modulo, fase = np.abs(X), np.angle(X, True)
ff = my.DFTFrec(N,Fs)

#Comprobacion con FFT
startFFT = time.time()
F = np.fft.fft(tension)
endFFT=time.time()

frec = np.fft.fftfreq(N, 1/Fs)
modulo2, fase2 = np.abs(F), np.angle(F, True)


    #%% Presentación gráfica de los resultados
  

mpl.pyplot.close('all')
    
plt.figure(1)
line_hdls = plt.plot(tiempo, tension)
plt.title('Señal Senoidal:')
plt.xlabel('tiempo [segundos]')
plt.ylabel('Amplitud [V]')
#    plt.grid(which='both', axis='both')


plt.figure(2)
line_hdls = plt.stem(ff,modulo, 'b', label='DFT', use_line_collection = True)
line_hdls = plt.stem(frec, modulo2, 'r--', label='FFT', use_line_collection = True)
plt.title('Modulo')

plt.figure(3)
line_hdls = plt.stem(ff,fase,'b', label='DFT', use_line_collection = True)
line_hdls = plt.stem(frec, fase2,'r--', label='FFT', use_line_collection = True)
plt.title('Fase:')

plt.show()

print("Tiempo de Ejecucion DFT:", endDFT-startDFT, "Para N=", N)
print("Tiempo de Ejecucion FFT:", endFFT-startFFT, "Para N=", N)