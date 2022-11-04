
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
    
   
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # Essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # Lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # O tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Construa com amplitude 1.
    # Some as senoides. A soma será o sinal a ser emitido.
    # Utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # Grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal
    DTMF =  {
        '1' : [697,1209],
        '2' : [679,1336],
        '3' : [679,1477],
        '4' : [770,1209],
        '5' : [770,1336],
        '6' : [770,1477],
        '7' : [852,1209],
        '8' : [852,1336],
        '9' : [852,1477],
        '0' : [941,1336],
        'x' : [941,1209],
        '#' : [941,1477],
        'a' : [697,1633],
        'b' : [770,1633],
        'c' : [852,1633],
        'd' : [941,1633]
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

    graf=np.linspace(0.0, t, int(fs/100))
    

    print("Executando as senoides (emitindo o som)")
    print("Gerando Tom referente ao símbolo : {}".format(tecla))
    

    #sd.play(sinal,fs)
    #Exibe gráficos
    plt.plot(graf, sinal[0:441])
    SINAL.plotFFT( sinal, fs)
    plt.show()
    # aguarda fim do audio
    sd.wait()
    
    

if __name__ == "__main__":
    main()
