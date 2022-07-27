# Natália Sens Weise, 5ºsem, Análise de Algoritmos
arvore = "<5<7 <5 > 3<6 4>>>" #pré-ordem [5, 7, 11, 3, 4]
arvore = "<5<7 3<6 4>>>" #pré-ordem [7, 11, 3, 4]
arvore = "<5<7 3<6 >>>" #pré-ordem [7, 11, 3]
arvore = "<5<7 <1 9 > 3<6 4>>>" #pré-ordem [1, 7, 20, 4, 3]

matriz =[]
pilha = []
indices = []
contador = -1
simbolos=['<', '>']
qtdEspacos = 0

# calcula qnts espaços precisa deixar para formar uma matriz
for i in list(arvore):
    if i == '<':
        qtdEspacos+=1
qtdEspacos-=1

# converte pré-ordem em matriz
temp = qtdEspacos
for i in list(arvore):
    if i == '<':
        matriz.append([])
        contador+=1 
        # if contador!=1: matriz[contador].append(" ")
        c = 0
        while c < temp:
            matriz[contador].append(" ")
            c+=1
        temp-=1
        if temp==0:
            temp=qtdEspacos
    if i not in simbolos:
        matriz[contador].append(i)

# verifica qual a maior lista da matriz
tamanho = 0
for lista in matriz:
    if len(lista) > tamanho:
        tamanho = len(lista)

# faz todas as listas da matriz ficarem com o mesmo tamanho
for lista in matriz:
    while len(lista) < tamanho:
        lista.append(' ')

# soma os valores que estão nas mesmas posições de coluna
for coluna in range(tamanho):
    for linha in range(len(matriz)):
        if matriz[linha][coluna] != " ":
            if coluna in indices:
                valor = int(matriz[linha][coluna])
                pilha[indices.index(coluna)]+=valor
            else:
                pilha.append(int(matriz[linha][coluna]))
                indices.append(coluna)
print(pilha)