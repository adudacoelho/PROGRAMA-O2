import random

def geraMatriz(linhas, colunas, min, max):

 matriz = [] #Aqui vai a matriz final, poderia ser lista tb aqui e no return

 for l in range (linhas):
    linha = [] #linha daqui é diferente de linhas da função
    for c in range (colunas):
        numero = (random.randint(min, max))
        linha.append(numero)
    matriz.append(linha)

 return matriz

def main():

    linhas = int(input("Qual a quantidade de linhas? "))
    colunas = int(input("Qual a quantidade de colunas? "))
    min = int(input("Valor mínimo: "))
    max = int(input("Valor máximo: "))

    matriz = geraMatriz(linhas, colunas, min, max)
    for linha in matriz:
     print(linha)


main()