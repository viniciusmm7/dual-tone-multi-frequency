
#importe as bibliotecas
import re
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys
import math
import time 


#funções a serem utilizadas
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

#converte intensidade em Db, caso queiram ...
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

    print("Inicializando encoder")
    print("Aguardando usuário")
    print("Gerando Tons base")
    
   
 
    SINAL = signalMeu()
    

    fs=44100 
    A = 1
    t = 2 #Tempo

    tecla = SINAL.discar(DTMF)

    freq_1,freq_2 = SINAL.dtmf(tecla,DTMF)
    s_1 = SINAL.senoid(freq_1,A,t,fs)
    s_2 = SINAL.senoid(freq_2,A,t,fs)
    sinal = SINAL.signal(s_1,s_2)

    tempo =np.linspace(0.0, t, int(fs/100))
    

    print("Executando as senoides (emitindo o som)")
    print("Gerando Tom referente ao símbolo : {}".format(tecla))
    

    sd.play(sinal,fs)
    #Exibe gráficos
    plt.plot(tempo, sinal[0:441])
    SINAL.plotFFT( sinal, fs)
    plt.show()

    sd.wait()
    
    

if __name__ == "__main__":
    main()
