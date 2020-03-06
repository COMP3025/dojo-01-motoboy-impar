def let(arq):   
    file = open(arq,'r')
    if file.mode == 'r':
        text = file.read()
        linha = text.split('\n')      
    return linha  

a = let('entrada.txt')

retorno = []
def reme(lista): 
    while True:
        tam = int(lista[0])
        retorno.append(lista[:tam+2])  
        lista = lista[tam+2:]
        if len(lista) <= 0:
            break
    return retorno   

def combinacao(arqs):
    for arq in arqs[:len(arqs)-1]:

        tempo = []
        pedidos = []

        pizzaMax = 0

        for i in range(0, len(arq)):

            if(i == 1):
                pizzaMax = int(arq[i])
            elif(i > 1):
                linha = arq[i].split(' ')

                tempo.append(linha[0])
                pedidos.append(linha[1])   

        listaSomaTempo = []
        for i in range(0, len(tempo)):
            somaPizza = 0
            somaTempo = 0

            for k in range(i, len(pedidos)):
                pedidos[k] = int(pedidos[k])
                tempo[k] = int(tempo[k])

                condicao = somaPizza + pedidos[k]

                if(condicao <= pizzaMax):
                    somaPizza += pedidos[k]
                    somaTempo += tempo[k]
                    listaSomaTempo.append(int(somaTempo))

                    if(somaPizza == pizzaMax):
                        somaPizza -= pedidos[k]
                        somaTempo -= tempo[k]
        print(max(listaSomaTempo), 'min')

b = reme(a)
combinacao(b)

