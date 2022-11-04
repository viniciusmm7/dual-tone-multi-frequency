#Importe todas as bibliotecas
from suaBibSignal import *
import peakutils    #alternativas  #from detect_peaks import *   #import pickle
import numpy as np
import sounddevice as sd
import matplotlib

import matplotlib.pyplot as plt
import time


#funcao para transformas intensidade acustica em dB, caso queira usar
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)


def main():

    DTMF = {
        '1': [697, 1209], '2': [697, 1336], '3': [697, 1477], 'A': [697, 1633],
        '4': [770, 1209], '5': [770, 1336], '6': [770, 1477], 'B': [770, 1633],
        '7': [852, 1209], '8': [852, 1336], '9': [852, 1477], 'C': [852, 1633],
        'X': [941, 1209], '0': [941, 1336], '#': [941, 1477], 'D': [941, 1633]
    }
    SINAL = signalMeu()
    sd.default.samplerate = 44100
    sd.default.channels = 2
    duration = 3
    
    numAmostras = duration * sd.default.samplerate
    freqDeAmostragem = sd.default.samplerate

    print('A captação começará em 3 segundos')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('\n==================')

    print('A gravação começou')
    audio = sd.rec(int(numAmostras), freqDeAmostragem, channels=1)
    sd.wait()
    print("...     FIM")


    freq_baixas = [697,770,852,941]
    freq_altas = [1209,1336,1477,1633]

        
    
    tempo = np.linspace(0.0, duration, duration*freqDeAmostragem)
    x,y = SINAL.calcFFT(audio[:,0],freqDeAmostragem)

    # Frequência no Tempo
    plt.plot(tempo,audio[:,0])
    plt.title('Frequência no Tempo')
    plt.show()

    # Fourier
    plt.plot(x, y)
    plt.title('Fourier')
    plt.show()
    
 
    index = peakutils.indexes(y, thres=0.4, min_dist=50)
    print(f"index de picos {index}") #yf é o resultado da transformada de fourier

    picks = []
    for freq in x[index]:
        picks.append(freq)



    tolerancia = 50

    f1 = 0; f2 = 0
    for pico in picks:
        for value in freq_baixas:
            if value-tolerancia < pico < value+tolerancia:
                f1 = value
        for value2 in freq_altas:
            if value2-tolerancia < pico < value2+tolerancia:
                f2 = value2
                
      
    teclas = list(DTMF.keys())
    sons = list(DTMF.values())  



    for t in sons:
        # print([int(f1),int(f2)])
        if [int(f1),int(f2)] in sons:
            tec = sons.index([f1,f2])


    print(f'a tecla pressionada foi: {teclas[tec]}')


  
    # Exiba gráficos do fourier do som gravados 
    plt.show()

if __name__ == "__main__":
    main()
