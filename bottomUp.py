# Natália Sens Weise, 5 sem, Análise de Algoritmos
# import sys
# sys.setrecursionlimit(5000)
import time
# inicia marcação de tempo
start = time.time()
print("Tempo inicial:"+str(start))


# método da mochila recursivo
def recursiveBackpack(n, v, w, W):
    if n == 0 or W == 0:
        return 0
    elif w[n-1] > W:
        return recursiveBackpack(n-1, v, w, W)
    else:
        use = v[n-1] + recursiveBackpack(n-1, v, w, W - w[n-1])
        dontUse = recursiveBackpack(n-1, v, w, W)
        return max(use, dontUse)

# monta a estrutura da matriz
def matrixGenerator(n, W):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(W):
            matrix[i].append(" ")
    return matrix

# método bottomUp mochila
def bottomUp(n, v, w, W):
    matrix = matrixGenerator(n, W)
    for x in range(W):
        matrix[0][x] = 0
    for j in range(n):
        matrix[j][0] = 0
    for j in range(1, n):
        for x in range(W):
            if w[j-1] > x:
                matrix[j][x] = matrix[j-1][x]
            else:
                use = v[j-1] + matrix[j-1][x-w[j-1]]
                dontUse = matrix[j-1][x]
                matrix[j][x] = max(use, dontUse)

    return matrix

# retira as infos necessárias do arquivo
def readingFile(fileName, weights, values, totalWeight, qtd):
    fileOpening = open(fileName, 'r')
    fileLines = fileOpening.read().split('\n')
    qtdElements = 0
    for i in fileLines:
        if fileLines.index(i) == 0:
            w = i.split("\t")
            total = int(w[0])
        if "	" in i and fileLines.index(i) != 0:
            qtdElements+=1
            w = i.split("	")[0]
            v = i.split("	")[1]
            weights.append(int(w))
            values.append(int(v))
    qtd.append(qtdElements)
    totalWeight.append(total)

# imprime a matriz num formato mlr de visualizar
def printMatriz(matrix):
    for i in matrix:
        print(i)


weights=[]
values=[]
totalWeight = []
qtd = []
readingFile('files/mochila5000.in', weights, values, totalWeight, qtd)
backpackWeight = totalWeight[0]
qtdItems = qtd[0]
print("Mochila 10 - Método Recursivo")
printMatriz(bottomUp(qtdItems, values, weights, backpackWeight))
# print(recursiveBackpack(qtdItems, values, weights, backpackWeight))

# weights = [2, 3, 6]
# values = [3, 6, 9]
# printMatriz(bottomUp(3, values, weights, 11))
# print(recursiveBackpack(3, values, weights, 11))

# calcula o tempo em que chegou aqui
end = time.time()
print("Tempo final:"+str(end))
# imprime a diferença dos tempos pra obter a duração
print("Tempo de execução:" + str(end - start))