## Executar nas maquinas
```
worker$ cd ~ && git clone https://github.com/fabiosammy/python_redis_multiprocess.git
worker$ sudo apt-get update
worker$ sudo apt-get install python-pip python-redis
worker$ sudo pip install rq
worker$ cd ~/python_redis_multiprocess/
```

#### Verifiquem se o redis esta rodando
```
master$ docker run --rm --network="host" -p 6379:6379 redis
```

#### Agora alterem o arquivo `redis_worker` para apontar o serviço redis da sua máquina (processo master)
```
worker$ python redis_worker.py
```

#### E por fim, rodem o processo master em sua máquina
```
master$ python redis_master.py
```

