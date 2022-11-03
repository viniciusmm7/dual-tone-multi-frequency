
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
    

    print("Inicializando encoder")
    print("Aguardando usuário")
    print("Gerando Tons base")
    
    DTMF ={
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
    keys = {
        "C":[264,2*264],
        "C#":[277.2,277.2*2],
        "D":[297,2*297],
        "D#":[311.1,311.1*2],
        'E':[330,660],
        'F':[352,253*2],
        "F#":[370,370*2],
        'G':[396,396*2],
        "G#":[415.3,415.3*2],
        'A':[440,880],
        "A#":[466.2,466.2*2],
        'B':[495,495*2]
    }



    SINAL = signalMeu()
    while True:
        tecla = input("Qual numero digital: ")
        if tecla in DTMF.keys():
            break

    fs=44100

    freq_1= DTMF[tecla][0]
    freq_2= DTMF[tecla][1]

    t = 2
    sinal_1 = SINAL.generateSin(freq_1, 0.3, t, fs)
    sinal_2  = SINAL.generateSin(freq_2, 0.3, t, fs)

    do = SINAL.generateSin(keys['C'][1], 0.3, t, fs)
    do_s = SINAL.generateSin(keys['C#'][1], 0.3, t, fs)
    re = SINAL.generateSin(keys['D'][1], 0.3, t, fs)
    re_s = SINAL.generateSin(keys['D#'][1], 0.3, t, fs)
    mi = SINAL.generateSin(keys['E'][1], 0.3, t, fs)
    fa = SINAL.generateSin(keys['F'][1], 0.3, t, fs)
    fa_s = SINAL.generateSin(keys['F#'][1], 0.3, t, fs)
    sol = SINAL.generateSin(keys['G'][1], 0.3, t, fs)
    sol_s = SINAL.generateSin(keys['G#'][1], 0.3, t, fs)
    la = SINAL.generateSin(keys['A'][1], 0.3, t, fs)
    la_s = SINAL.generateSin(keys['A#'][1], 0.3, t, fs)
    si = SINAL.generateSin(keys['B'][1], 0.3, t, fs)


    do_maior = do + mi + sol
    fa_maior = fa + la + do
    sol_m = sol + si + re


    tom = sinal_1+sinal_2
    print("Executando as senoides (emitindo o som)")
   # print("Gerando Tom referente ao símbolo : {}".format(NUM))

    sd.play(tom,fs)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()
    SINAL.plotFFT( tom, fs)
    

if __name__ == "__main__":
    main()
