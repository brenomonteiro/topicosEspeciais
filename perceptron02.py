from random import uniform
def calcular(x,w):
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
x = [1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],[1,1,1,0],[1,1,1,1]

#print(type(matrizAmostra))


w = [0,0,0,0]


d = [-1,-1,-1,-1,-1,-1,-1,1]

#for l in range(len(x[0])):
   # w.append(uniform(-1,1))


n = 0.5

epocas = 0
print('x0',x[0])
print('peso inicial',w)
while True:
    erro = False
    for k in range(len(x)):
        u = calcular(x[k],w)
        y = calcularFuncTransferencia(u)
        print(x[k])

        
        print("desejado =  ", d[k], " e y = ", y)
        if y != d[k]:
            erro = True

            for i in range(len(w)):
                w[i] = w[i]+ n * (d[k]-y) * x[k][i]
                print(x[k][i])

    if erro == False:
        break
    
    epocas = epocas + 1
    print("Epocas ", epocas)

#fase validação
parar = False



while parar==False:
    entrada = [1]
    for x in range(3):
        x1 = input('digite a entrada '+str(x+1))
        entrada.append(int(x1))
        print('print entrada: ',entrada)

    u = calcular(entrada,w)
    y = calcularFuncTransferencia(u)
    print('y aqui',y)

    
print('peso final',w)
print("Rede Treinada!!!")
print("Quantidade de épocas: ",epocas)
