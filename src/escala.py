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
