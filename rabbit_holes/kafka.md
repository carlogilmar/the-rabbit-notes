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
