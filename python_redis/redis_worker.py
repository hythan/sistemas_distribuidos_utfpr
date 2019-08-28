from redis import Redis
from rq import Worker, Queue, Connection

listen = ['my_queue']

if __name__ == '__main__':
  redis_conn = Redis(host='127.0.0.1',port=6379)
  with Connection(redis_conn):
    worker = Worker(map(Queue, listen))
    worker.work()
