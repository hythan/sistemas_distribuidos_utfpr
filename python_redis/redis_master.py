from time import sleep
from redis import Redis
from rq import Queue
import numpy
import time
from multiprocessing import JoinableQueue
import multiprocessing

from redis_modules import cria_matriz, multiplica_linha_coluna

if __name__ == "__main__":
  print "Initializing redis master"
  redis_conn = Redis(host='127.0.0.1',port=6379)
  queue_jobs = Queue('my_queue', connection=redis_conn)

  linhas, colunas = 3, 3

  print("{}: Gerando matrizes".format(time.strftime('%c')))
  matrizA = cria_matriz(linhas, colunas)
  matrizB = cria_matriz(linhas, colunas)
  matrizC = numpy.zeros(shape=(linhas,colunas))

  print("{}: Multiplicando matrizes".format(time.strftime('%c')))

  jobs = []
  for i in range(len(matrizA)):
    for j in range(len(matrizB)):
      job = queue_jobs.enqueue(multiplica_linha_coluna, matrizA ,matrizB , i, j)
      jobs.append(job)
      

    for job in jobs:
      print "Trabalhos enfileirados {0}".format(len(queue_jobs))
      while job.result is None:
        print "O trabalho {0} ainda nao foi concluido".format(job.id)
        sleep(2)
        print "Resultado {0}".format(job.result)
      print job.result
      linha, coluna, valor = job.result
      matrizC[linha][coluna] = valor
        

    

print("{}: Resultado:{}".format(time.strftime('%c'), matrizC))
