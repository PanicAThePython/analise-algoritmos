# Natália Sens Weise, 5ºsem, Análise de Algoritmos
lucro = 0
pesoTotal = 8
lista = [[40, 2], [70, 2], [140, 3], [100, 3], [130, 4], [230, 4], [110, 5], [80, 2]]
subconjuntos = []

for i in range(0, 256):
    subconjuntos.append(format(i, "b").zfill(8))

def maiorLucro(lucro, pesoTotal, subconjuntos, somaPesos=''):
    for i in subconjuntos:
        # pesosMochila=""
        peso = 0
        valor = 0
        binarios = list(i)
        for i in range(len(binarios)):
            if binarios[i]=='1':
                valor+=lista[i][0]
                peso+=lista[i][1]
                # pesosMochila+=str(lista[i][1])+" "
        if peso <= pesoTotal:
            if valor > lucro:
                lucro = valor
                # somaPesos=pesosMochila
    # print(somaPesos) #mostra os pesos que geram o mlr lucro
    return lucro

print(maiorLucro(lucro, pesoTotal, subconjuntos))