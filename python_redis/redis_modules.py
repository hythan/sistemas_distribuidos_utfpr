from time import sleep
from multiprocessing import JoinableQueue
import random

def cria_matriz(linhas, colunas):
  A = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha = linha + [random.randint(1, 10)]
    A = A + [linha]
  return A


def multiplica_linha_coluna( matrizA, matrizB, i, j):
      valor = 0
    
      for k in range(len(matrizB)):
           valor = valor + matrizA[i][k] * matrizB[k][j]
      return i, j, valor

