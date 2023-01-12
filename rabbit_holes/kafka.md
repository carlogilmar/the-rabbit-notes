# Kafka

## Event Streaming

> **Event streaming** is the practice of capturing data in real-time from event sources 
> like databases, sensors, mobile devices, cloud services, and software applications 
> in the form of streams of events; storing these event streams durably for later retrieval; 
> manipulating, processing, and reacting to the event streams in real-time
> as well as retrospectively; and routing the event streams to different destination 
> technologies as needed. 

## Kafka

Kafka combines three key capabilities so you can implement your use cases for event streaming end-to-end with a single battle-tested solution:

1. To publish (write) and subscribe to (read) streams of events, including continuous import/export of your data from other systems.
2. To store streams of events durably and reliably for as long as you want.
3. To process streams of events as they occur or retrospectively.

Kafka is a distributed system consisting of servers and clients that communicate via a high-performance TCP network protocol. It can be deployed on bare-metal hardware, virtual machines, and containers in on-premise as well as cloud environments.

Concepts:

- An **event** records the fact that "something happened" in the world or in your business. 
- **Producers** are those client applications that publish (write) events to Kafka
- **Consumers** are those that subscribe to (read and process) these events. 

## Installation using Docker

[Kafka Installation Docker M1](https://www.conduktor.io/kafka/how-to-start-kafka-using-docker)

1. Clone the repo `https://github.com/conduktor/kafka-stack-docker-compose`.
2. Launch the cluster: `docker-compose -f zk-single-kafka-single.yml up -d`
3. Check docker services running: `docker-compose -f zk-single-kafka-single.yml ps`
4. Kafka is exposed at `localhost:9092`.
5. For run inside the container `docker exec -it kafka1 /bin/bash`.
6. Stop the container: ` docker-compose -f zk-single-kafka-single.yml stop`

## More theory

![image](https://user-images.githubusercontent.com/17634377/212158175-24275b59-ddc1-4b6e-8c68-75cb41340c59.png)

Integrations comes with difficulties around:

- Protocol – how the data is transported (TCP, HTTP, REST, FTP, JDBC…)
- Data format – how the data is parsed (Binary, CSV, JSON, Avro…)
- Data schema & evolution – how the data is shaped and may change

![image](https://user-images.githubusercontent.com/17634377/212158221-fabab02d-0190-44b7-9ad7-a9c984397091.png)


