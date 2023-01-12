# Making reliable distributed systems in the presence of software errors

*Joe Armstrong Thesis, 2003.*

**How can we program systems which behave in a reasonable manner in the presence of software errors?**

## Chapter 1: Introduction to Erlang Development

- Erlang belongs to the family of pure message passing languages—it is a concurrent process-based language having strong isolation between concurrent processes. 
- The work reported here was performed in the period 1981-2003. During this time the Erlang programming language and OTP was developed by the author and his colleagues.
- The language started as an experiment to add concurrent processes to Prolog.
- I was interested in how to program POTS (Plain Old Telephony Service) using Prolog.
- ACS was a prototype and an architecture which was designed for implementing the **Ericsson MD110** private automatic branch exchange (PABX) using the Erlang implementation in Prolog. (Many of the ideas found in the current Erlang/OTP system can be traced back to this project.)
- 1987 — First mention of Erlang
- 1989 — The ACS/Dunder project began to produce results. 

**Ericsson MD110**

![image](https://user-images.githubusercontent.com/17634377/211988182-e155491c-5e89-4134-8681-a528e285e9a6.png)

- Erlang Versions
  - Erlang I was an implementation in prolog.
  - To improve the performance of Erlang I designed the JAM machine (Joe’s abstract machine).
  - The design of the JAM machine was loosely based on the Warren abstract machine WAM.
  - The JAM machine was similar to the WAM with the addition of parallel processes, message passing and failure detection and with the omission of backtracking
  - The design of the JAM was completed in 1989.
  -  Mike Williams wrote the virtual machine emulator and Robert Virding worked on the Erlang libraries.
  -  By 1990 the JAM machine was working well and had surpassed the original goal of being seventy times faster than the original Prolog interpreter (written in C).
  -  1993: Ericsson starts a wholly owned subsidiary company called Erlang Systems AB.
  -  1995: A switch project in Ericsson collapse and they restarted the project using Erlang. This project eventually resulted in the development of the AXD301 switch.
  -  A new group was started to provide support to the AXD project. The Erlang libraries were renamed OTP (The Open Telecom Platform) and a new group was created.
  -  The OTP project consolidated a number of ideas derived from experience with Erlang and in particular from a earlier set of libraries developed for use in the Mobility Server.
  -  1998 — Ericsson delivered the first AXD301.

![image](https://user-images.githubusercontent.com/17634377/211989172-2b2afb73-b855-472f-bdab-d26d8cd160da.png)

- In February 1998 Erlang was banned for new product development within Ericsson—the main reason for the ban was that Ericsson wanted to be a consumer of sodware technologies rather than a producer.
- In December 1998 Erlang and the OTP libraries were released subject to an Open Source License.
- In 1998 I led Ericsson and I found a new company Bluetail AB—in all 15 people led Ericsson. The idea was to use the Erlang technology to program products which make Internet services more reliable.
- 2001 — The Erlang/OTP technology is well established
  

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
