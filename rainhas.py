# Natália Sens Weise, 5sem, Análise de Algoritmos
import random
positions = [1, 3, 5, 2, 7, 8, 6, 8]

# monta a estrutura da matriz
def matrixGenerator(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    return matrix

# colocando os elementos nas posições
def populate(positions, matrix):
    for i in range(len(matrix)):
        if i+1 in positions:
            cont = positions.count(i+1)
            index = positions.index(i+1)
            if cont == 1:
                matrix[i][index] = 1
            else:
                while cont > 0:
                    matrix[i][index] = 1
                    cont-=1
                    if cont > 0: index = positions.index(i+1, index+1, len(matrix))
            
    return matrix

# calcula colisões dentro da linha
def calculateHorizontalCollisions(matrix, collisionList):
    collisions = 0
    repeatedIndexes = []
    for i in matrix:
        cont = i.count(1)
        if cont > 1:
            collisions+=1
            repeatedIndexes = [j for j, item in enumerate(i) if item == 1]
        collisionList.append(collisions)
    for i in repeatedIndexes:
        collisionList[i] = 1

# calcula colisões na mesma coluna
def calculateVerticalCollisions(matrix, collisionList):
    for i in range(len(matrix)):
        collisions = 0
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                collisions+=1
        collisions-=1
        collisionList[i]+=collisions

# calcula colisões na diagonal
def calculateDiagonalCollisions(matrix, collisionList, coordenates):
    control = -1
    for i in range(len(matrix)):
        control+=1
        for j in range(len(matrix)):
            collisions=0
            if matrix[j][i] == 1:
                line = j
                column = i
                coordenates.append([line, column])
                contador=1
                while contador+line< len(matrix) and contador+column < len(matrix):
                    if matrix[line+contador][column+contador] == 1:
                        collisions+=1
                    contador+=1
                contador=1
                while line-contador>= 0 and column-contador>=0:
                    if matrix[line-contador][column-contador] == 1:
                        collisions+=1
                    contador+=1

                contador=1
                while contador+line< len(matrix) and column-contador>=0:
                    if matrix[line+contador][column-contador] == 1:
                        collisions+=1
                    contador+=1

                contador=1
                while line-contador>= 0 and contador+column < len(matrix):
                    if matrix[line-contador][column+contador] == 1:
                        collisions+=1
                    contador+=1
                collisionList[control]+=collisions
                

# chama todas as formas de colisão e retorna a lista de colisões conforme coluna
def calculateCollisions(matrix, coordenates):
    collisionList = []
    calculateHorizontalCollisions(matrix, collisionList)
    calculateVerticalCollisions(matrix, collisionList)
    calculateDiagonalCollisions(matrix, collisionList, coordenates)
    return collisionList

# redefine a matriz quando ainda houver colisões
def redefineMatrix():
    change = coordenates[collisionsList.index(max(collisionsList))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == change[0] and j==change[1]:
                matrix[i][j] = 0
                for z in [random.randrange(8)]:
                    matrix[z][j] = 1
                    break

# marca as novas posições numa lista
def definingNewPositions(matrix):
    newPositions = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                newPositions.append(j+1)
    return newPositions

# imprime a matriz num formato mlr de visualizar
def printMatrix(matrix):
    for i in matrix:
        print(i)

coordenates = []
matrix = populate(positions, matrixGenerator(8))
initialMatrix = populate(positions, matrixGenerator(8))
collisionsList = calculateCollisions(matrix, coordenates)
cont = collisionsList.count(0)
counter=0
limiter = 50000
# print(definingNewPositions(matrix))
# print('\n')
# printMatrix(matrix)
# print('\n')
# print(collisionsList)
while counter < limiter and cont != len(matrix):
    counter+=1
    redefineMatrix()
    coordenates = []
    collisionsList = calculateCollisions(matrix, coordenates)
    # print(definingNewPositions(matrix))
    # print('\n')
    # printMatrix(matrix)
    # print('\n')

    if counter==limiter and cont != len(matrix):
        print("Desculpe, não consegui achar uma solução para as colisões")

    elif cont == len(matrix):
        print("Achei a resposta!")
        print("\n")
        print("Inicial")
        print("-----------------")
        print(positions)
        printMatrix(initialMatrix)
        print("\n")
        print("Final")
        print("-----------------")
        print(definingNewPositions(matrix))
        printMatrix(matrix)