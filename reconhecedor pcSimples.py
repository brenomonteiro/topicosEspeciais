from random import uniform
def calcular(x, w):
    u = 0
    for i in range(len(x)):
        u = u + x[i] * w[i]
    return u

def calcularFuncTransferencia(u):
    teta=-0.3
    if u>teta:
        return 1
    elif u<-teta:
        return -1
    else:
        return 0


#amostras
x = [
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], 
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
]

w = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


#d = [-1, -1, -1, -1, -1, -1, -1, 1]
d = [
    [1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, 1, -1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, 1, -1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, 1, -1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, 1, -1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, -1, 1, -1], 
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, 1]
]

u = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


n = 0.5

epocas = 0
while True:
    erro = False
    for k in range(len(x)):
        for p in range(len(w)):
            u[p] = calcular(x[k], w[p])
            y[p] = calcularFuncTransferencia(u[p])

            if y[p] != d[k][p]:
                erro = True
                for i in range(len(w[p])):
                    w[p][i] += n * ((d[k][p] - y[p]) * x[k][i])

    if erro == False:
        break
    
    epocas = epocas + 1
    print("epoca",  epocas)

print("Rede Treinada com  {} epocas!".format(epocas))



#fase validação

xteste = [0, 0, 0,0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
            

for p in range(len(w)):
    u[p] = calcular(xteste, w[p])
    y[p] = calcularFuncTransferencia(u[p])

print("predição {} fase de validação".format(y.index(1)))
