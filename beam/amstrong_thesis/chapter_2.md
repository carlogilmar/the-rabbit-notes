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

### Concurrency Oriented Programming
