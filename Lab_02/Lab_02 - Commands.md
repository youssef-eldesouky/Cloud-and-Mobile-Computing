## Distributed Consistency and Consensus

1. ```docker-compose up -d```

2. ```docker ps```

3. ```docker exec -it lab_02-redis-node2-1 redis-cli replicaof redis-node1 6379```

4. ```docker exec -it lab_02-redis-node1-1 redis-cli set my_key "hello_redis"```

5. ```docker exec -it lab_02-redis-node2-1 redis-cli get my_key```

6. ```docker exec -it lab_02-etcd-1 etcdctl put lab_status "active"```

7. ```docker exec -it lab_02-etcd-1 etcdctl endpoint status --write-out=table```
