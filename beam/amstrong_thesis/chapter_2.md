## Chapter 2: The Architecture Model

> An architecture is the set of significant decisions about the organization of a software system, the selection of the structural elements and their interfaces by which the system is composed and the architectural style that guides this organization—these elements and their interfaces, their collaborations, and their composition.

An architecture is “a way of thinking about the world.”:
1. Problem domain
2. Philosophy
3. Construction guidelines
4. Set of pre-defined components
5. A way of describing things
6. A way of configure things

### Problem Domain
- Our system was originally designed for building telecoms switching systems.
- Dacker gave ten requirements for the properties of a telecoms system:
  1. The system must be able to handle very large numbers of concurrent activities.
  2. Actions must be performed at a certain point in time or within a certain time.
  3. Systems may be distributed over several computers.
  4. The system is used to control hardware.
  5. The software systems are very large.
  6. The system exhibits complex functionality such as, feature interaction.
  7. The systems should be in continuous operation for many years.
  8. Software maintenance (reconfiguration, etc) should be performed without stopping the system.
  9. There are stringent quality, and reliability requirements.
  10. Fault tolerance both to hardware failures, and sodware errors, must be provided.
- This requirements are rewritted as:
  - **Concurrency:** switching systems are inherently concurrent since in a typical switch many tens of thousands of people may simultaneously interact with the switch.
  - **Soft real-time**: — in a telecommunications system many operations have to be performed within a specific time.
  - **Distributed:** our system should structured in such a way that it is easy to go from a single-node system to a multi-node distributed system.
  - **Hardware interaction** — Switching systems have large amounts of peripheral hardware which must be controlled and monitored.
  - **Large software systems** — switching systems are large, for example, the Ericsson AXE10, and the AT&T 5ESS switch, have several million lines of program code
  - **Complex functionality** — switching systems have complex functionality.
  - **Continuous operation** — telecommunications systems are designed for many years of continuous operation.
  - **Quality requirements** — switching systems should run with an acceptable level of service even in the presence of errors.
  - **Fault tolerance** — we must design a software and hardware infrastructure that can deal with these faults

### Philosophy

> Fault tolerant systems in presence of software errors.

1. `Tasks`: We organise the software into a hierarchy of tasks that the system has to perform.
  - Each task corresponds to the achievement of a number of goals.
  - The software for a given task has to achieve the goals associated with the task.
  - Tasks are ordered by complexity. Top level task is the most complex. Lower level tasks should allow the system to function in an acceptable manner.
2. `Perform`: We try to perform the top level task.
3. `Errors`: If an error is detected when trying to achieve a goal, we make an attempt to correct the error. If we can't correct the rror, we about the current task and start performing a simpler task.

Notes about this:

- Programming a hierarchy of tasks needs strong encapsulation method.
- We need strong encapsulation for error isolation.
- We need to isolate all the code that runs in order to achieve a goal.
- When we are trying to simultaneously achieve multiple goals we don't want a error ocurring and propagate to another part of the system.
- The essential problem about fault-tolerant systems is the fault-isolation.
  - We don't want the errors in one module affect the behaviour of a module which doesn't have any errors.
  - We use the traditional operating system notion of a process.
  - Processes provide protection domains.
  - Errors in one application (built by processes) shouldn't have a negative influence on other applications running in the system.
  - To extend to which processes can interfere with each other depends upon the design characteristics of the operating system.
  - Advantages over operating system processes built in our system processes
    - Concurrent programs run identically on different OS.
    - We're not limited by how processes are implemented on any particular operating system.
    - Question? How the SO. and the BEAM is managing the processes into SO processes?
    - The different betweer SO processes and processors are the CPU speeds and memory sizes.
    - Our language based processes are lighter-weight than conventional OS processes.
    - Creating processes is a highly efficient operation. (much faster than process creation in SO and than thread creation)
    - The Erlang system use of very few operating system services.

- Our applications are structured using parallel processes:
  - It provides an architectural infrastructure.
  - By enumerating all the processes in our system we can partition the system into a number of well-defined subcomponents which can be independently implemented and tested.
  - A system which is designed to be implemented as independent concurrent processes can be implemented on a multiprocessor or run on a distributed network.
  - Concurrent processes with no data sharing provide a strong measure of fault isolation.

### Concurrency Oriented Programming COP

- Content structure of the program should follow the concurrent structure of the application.
- COP provides the two major advantages associated with Object-oriented programming: polymorphism and the use of protocols having the same message passing interface.
- We can partition a problem into a number of concurrent processes, all process respond to the same messages (they are polymorphic) and they all follow the same message passing interface.
- `Concurrency` is used to refers to sets of events which happen simultaneously.
- Real world is concurrent. Sequential activities are a ratity.
- Programming a sequential chain of activities is viewed the norm, whereas programming collections of concurrent activities is avoided as much as possible.
- There are poor support provided for concurrency in virtually all conventional programming languages.
- Concurrency is provided by the programming language and not by the operating system.

### Programming by observing the real world

Analysis:

1. We identify all the concurrent activities in our real world activity.
2. We identify all message channels between the concurrent activities.
3. We write down all the messages which can flow on the different message channels.

Notes:
- The structure of the program should exactly follow the structure of the problem.
- Each concurrent activity should be mapped onto one concurrent process.
- 1:1 mapping minimizes the conceptual gap between the problem and the solution.
- non-COP languages are difficult because they don't have this mapping.

### Concurrent Oriented Programming Characteristics

1. Must support processes. `A process can be thought af as a self-contained virtual machine`.
2. Many processes operating on the same machine must be strongly isolated. A fault in one process hsould not adversely aeffect another process.
3. Each process must be identified by a unique unforgeable identifier.
4. There shoulb be no shared state between processes. Processes interact by sending messages.
5. Message passing is assumed to be unreliable with no guarantee of delivery.
6. It should be possible for one process to detect failure in another process. We should also know the reason for failure.

More notes:
- COP must provide true concurrency.
- Objects represented as processes truly concurrent.
- Messages are true asynchronous messages.

### Process Isolation

- This term is central to understanding COP and the construction of fault-tolerant software.
- Two processes operating on the same machine must be as independent.

Consequences of process isolation:

1. Processes have share nothing sematincs. (They run on physically separated machines)
2. Message passing is the only way to pass data between processes. Nothing is shared.
3. Isolation implies that message passing is asynchronous. (To avoid block any flow)
4. Everything necessary to perform a distributed computation must be copied.

**Names of processes:**
- We requiere names of processes are unforgeable.
- Processes know their own names.
- Parent process knows the names of it's children.
- If we know the name of a process, we can send a message to that process.
- If we cannot know the name of a process we cannot interact with it.

**Message Passing:**
- It's assumed to be atomic, when a message is delivered in it's entirety or not at all.
- Message passing between a pair of process is to be ordered meaning that if a sequence of messages is sent and received, in the same order they were sent.
- Messages should not contain pointers to data structures contained within processes.
- We can send the message and pray that it arrives.
- Confirmation that a messages has arrived can be achieved by returning a confirmation message.
- Message Passing is also used for synchronisation.  `Casual Ordering`

### Protocols

- We need isolation of components, message passing and communication protocols.

### System Requirements for Concurrency Oriented Programming

1. System must support concurrency.
2. Error encapsulation
3. Fault detection.
4. Fault identification.
5. Code Upgrade.
6. Stable storage.

### Language Requirements

1. Encapsulation primitives: mechanisms for limiting the consequences of an error.
2. Concurrency: must support a lightweight mechanism to create parallel process and send messages between the processes.
3. Fault detection primitives: alow one process to observe another process.
4. Location transparency: if we know the PID of a process, then we should be able to send a message to the process.
5. Dynamic code upgrade: it should be possible to dynamically change code in a running system. We need a mechanism to allow existing processes to run old code and for new processes to run the modified code at the same time.

### Library Requirements

The essential set of libraries routines must provide:

- Stable stoage which survives a crash.
- Device drivers: communication with the outside world.
- Code upgrade: upgrade code in a sunning system.
- Infrastructure: starting and stopping the system...
- The library routines are conventionally provided by an operating system.
- The remaining OS only provides a primitive set of device drivers.

## Application libraries

- Complex applications need much higher-level abstractions than storage.
- We need pre-packaged software entities to help us program.

> OTP libraries provide us with a complete set of design patterns (behaviours) for building fault-tolerant applications

**OTP Behaviours:**

1. Supervisor
2. Gen Server
3. Gen Event
4. Gen_fsm Finite State machine


