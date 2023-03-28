# Redis

# Redis Cluster

Follow this: https://redis.io/docs/management/scaling/#create-a-redis-cluster

1. Open every folder and run the redis server:

> redis-server ./redis.conf

2. Make sure that you don't have a `nodes.conf` file.
3. After run all your nodes, create the cluster:

```
redis-cli --cluster create 127.0.0.1:6000 127.0.0.1:6001 \
         127.0.0.1:6002 127.0.0.1:6003 127.0.0.1:6004 127.0.0.1:6005 \
         --cluster-replicas 1
```

4. Enjoy
