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
ff = my.DFTFrec(N, Fs)

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
# line_hdls = plt.stem(frec, modulo2, 'r--', label='FFT', use_line_collection = True)
plt.title('Modulo')

plt.figure(3)
line_hdls = plt.stem(ff,fase,'b', label='DFT', use_line_collection = True)
# line_hdls = plt.stem(frec, fase2,'r--', label='FFT', use_line_collection = True)
plt.title('Fase:')

plt.show()

print("Tiempo de Ejecucion DFT:", endDFT-startDFT, "Para N=", N)
print("Tiempo de Ejecucion FFT:", endFFT-startFFT, "Para N=", N)



##################
# Pruebas de tiempo en funcion de N
#################
fs = 1000
a0 = 1       # Volts
p0 = np.pi/2 # radianes
f0 = fs/2    # Hz

N = [16, 32, 64, 128, 256, 512, 1024, 2048]
tus_resultados = [['--']]
# Insertar aquí el código para generar la señal
##############################################################

# for nn in N:
#     tiempo, tension = my.mi_funcion_sen( a0, 0, f0, p0, nn, fs)
    
#     the_start = time.time()
#     my.DFT(tension)
#     the_end = time.time()

#     tus_resultados.append([str(the_end-the_start)])

# tus_resultados2 = [ ['1'], 
#                    ['2'], # <-- acá debería haber numeritos :)
#                    ['3'], # <-- acá debería haber numeritos :)
#                    ['4'], # <-- acá debería haber numeritos :)
#                    ['5'], # <-- acá debería haber numeritos :)
#                    ['6'], # <-- acá debería haber numeritos :)
#                    ['7'], # <-- acá debería haber numeritos :)
#                    ['8'], # <-- acá debería haber numeritos :)
#                    ['9']  # <-- acá debería haber numeritos :)
#                  ]
    
    