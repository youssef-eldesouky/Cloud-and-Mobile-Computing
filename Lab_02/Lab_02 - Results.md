# Lab 02: Distributed Consistency and Consensus Results

## Task 1: Redis Replication and CAP
In this task, we simulated eventual consistency by setting up a primary-replica relationship between two Redis nodes.

#### Commands Executed:
1. **Initialize Replica:**
   `docker exec -it lab_02-redis-node2-1 redis-cli replicaof redis-node1 6379`
2. **Write to Primary (node1):**
   `set my_key "hello_redis"`
3. **Read from Replica (node2):**
   `get my_key`

#### Observations:
- Data written to node1 was immediately available on node2 due to replication.
- During a simulated partition (stopping node2), node1 continued to accept writes, demonstrating availability over strict consistency in this configuration.


## Task 2: Raft with etcd
This task explored the Raft consensus protocol using etcd to manage distributed state.

#### Commands Executed:
1. **Put Key:**
   `etcdctl put lab_status "active"`
2. **Check Endpoint Status:**
   `etcdctl endpoint status --write-out=table`

#### Observations:
- The etcd node identifies itself as the leader in the Raft cluster.
- Consensus ensures that the state "active" is committed across the cluster before the write is acknowledged.
