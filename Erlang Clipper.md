## Erlang 

- Create a module
- Compile module from repl
- Call module functions
- Import hrl files

Mnesia Concepts

Schema: Configuration of the system, it´s a table with information with the table names and the storage type

Mnesia Functions for schema:
- Initializes an empty schema for start Mnesia
- Falls if a schema is already present in any node in the NodeList 
- Delete Schema
- Delete table
- Clear table
- Move table copy
- Add table copy
- Delete table copy
- Transform table

Data model: 

The data model is an extended relational data model. Data is organized as a set of tables and relation. Each table contains instances of Erlang represented records. The records are represented as Erlang tuples.

Start Mnesia mnesia:start() 

1. Empty schema initialized
2. Erlang system started
3. Nodes defined and implemented (NodeList)

Example Mnesia

1. Start Mnesia with the location of the database directory 
2. Create an empty schema
3. Start Mnesia
4. Run the module function for create the tables given by the company.hrl file
5. Run mnesia:info(). for see the database status

Monday 18
Meeting with Francesco and Ali

- How Wombat reacts in the Mnesia Partition
- Wombat Agent
- Add elixir examples
- Netslip in circle ci
- Trigger mnesia backups
- See how to backup 
- Visuailzation of the wombat

Wombat
- Install by package or docker image
- Docker hub erlang wombatoam
- Propietary License 
- Add nodes: add the name and the cookie
- Wombat agents are the plugins whom are going to be injected
- Metrics: total memory, process, mensages, atoms, binary in live
- Metrics, Nodes, ports, sockets, memory, IO, runtime, schedulers, error log
- It depends, it could monitor Cowboy request, response time, 
- Mnesia System Metrics: list of metrics, we don't know which are useful 
- Loger Notifications error_logger:error_msg("errrozzz").
- Individual metrics for a process
- Topology: Nodes: terminate process
- Table visualizer
- Data Export

Wombat

Learning Safari:

1. Installation
2. Adding a Node
3. Explore main information

- Home tab: Main actions over the node (evaluate erlang expression, garbage collector, recover from partition mnesia, purge old modules, terminate process, terminate shell processes)
- System: info about node name, cokkie, state, hardware, OS, Erlang VM
- Agents: agent plugins on/off

4. Node graph
5. Metrics

Questions:

1. I can't add a node from the erlang shell 
erl -sname test -setcookie abc123
net_adm:ping('test@MacBook-Pro-de-Carlo').

This is because there are a big issue with macos, the solution is running  shell inside the same wombat container 

2. How to start to explore the app with Wombat
3. Nodes/ Node graph
4. What's an agent?

To Do:

Monitor the mnesia network partition 

Docker Tricks

Create network

> docker network create -d bridge mnesia-net
> docker network ls
> docker network connect NETWORK CONTAINER
> docker network inspect mnesia-net -f "{{json .Containers }}"

Dockerfile for erlang

```
FROM centos
# Install basic utilities
RUN yum -y install gcc openssl-devel bzip2-devel libffi-devel zlib-devel tree wget curl make git ncurses-devel
# Download erlang
RUN wget http://erlang.org/download/otp_src_23.2.tar.gz
RUN tar -zxf otp_src_23.2.tar.gz && rm -rf otp_src_23.2.tar.gz
RUN cd otp_src_23.2 && ./configure && make && make install
```


Start Docker containers and connect to the network
```
cd ~/projects/mnesia_docker
docker stop mnesia1
docker rm -vf mnesia1
docker build -f Dockerfile -t hernan/mnesia1 .
docker run --network=mnesia-net --name mnesia1 -it hernan/mnesia1 bin/bash
```

```
cd ~/projects/mnesia_docker
docker stop mnesia2
docker rm -vf mnesia2
docker build -f Dockerfile -t hernan/mnesia2 .
docker run --network=mnesia-net --name mnesia2 -it hernan/mnesia2 bin/bash
```

Connect and disconnect

```
docker network disconnect mnesia-net mnesia1
docker network connect mnesia-net mnesia1
```

Start erlang on nodes
```
erl -setcookie mnesia -mnesia debug verbose -name mnesia1@172.18.0.3
erl -setcookie mnesia -mnesia debug verbose -name mnesia2@172.19.0.3
```

Saber las IP de los contenedores

```
docker inspect mnesia1
docker inspect mnesia2
```

Ping en shells 
```
net_adm:ping('mnesia2@172.19.0.3').
net_adm:ping('mnesia1@172.19.0.2').
```

Agregar records
```
rd(person, {name, age}).
mnesia:create_schema([node() | nodes()]).
mnesia:subscribe(system).
mnesia:subscribe(activity).
mnesia:start().

mnesia:create_table(person, []).
mnesia:transaction(fun() -> mnesia:write({person, hernan, 31}) end).

mnesia:dirty_read(person, hernan).

mnesia:set_master_nodes(person, [node()]).
mnesia:set_master_nodes(person, nodes()).

mnesia:transaction(fun() -> mnesia:write({person, carlo, 26}) end).

mnesia:stop().
mnesia:start().
```

### Mnesia Commands

```
set_debug_level(debug)
```


# Wombat OAM

## Getting Started Guide

1. Software propietary: needs a license key
2. Fastest way installation: by the package
3. Meet the web dashboard
4. Running Wombat: start, stop, use the scripts for additional options
5. Using wombat: add itself as a node, check the log, review memory metrics
6. Install WombatOAM in distributed mode
7. Environment Variables 
8. Mounting volumes to keep historical data in docker containers: data, log, key, config
9. Use on AWS
10. Running on Windows

## Exploring Wombat
1. Full visibility of what is happening, pre-emptive support, post mortem debugging, handy for troubleshooting, online diagnosing and resolving invidents on the fly
    1. Add a node
    2. Wombat is going to start agents that collects metrics, alarms, notifications
    3. Basic installation have plugins for: Exometer/folson metrics, automatic SASL logs, 25 alarms, confi, etop process listing, ets table viewer, process inspectos, executor for user commands or initiating garbage collector
    4. Usages: Kernel, OS_mon, poolboy, lager, exometer, cowboy, phoenix, ecto
    5. Topology tab -> System
    6. Simulate a problem that might occur
        1. Send 100 000 messages to the shell process (process dictionary)
        ``` 
        put(sample_key, value), [ self() ! {count, Int} || Int <- lists:seq(1,100000) ].
        ```
        2. Tools -> select your node -> Open Process Manager panel
        3. Check Shell Process
        4. Go to Metrics -> select your node -> Memory -> Total Memory & Process Memory
        5. Select alarms and note process_message_queue_major
        6. Back to Metrics -> Process -> Sum message queue length
        7. Click Live Metrics -> Sum message queue length
        8. In your shell enter `flush().` and you .will see this in the live metrics
        9. See notifications tab and alarms

Further Information: Alarms and notifications

1. Node down, Wombat will be alert. If the node is restarted, it will be added.

2. Stress the atom table: go to Alarms -> Your Node -> get atom_limit_major
```
[ list_to_atom("atom_" ++ integer_to_list(I)) || I <- lists:seq(1, 964689) ].
```

3. Too many ETS tables: ets_limit_major
```
[ ets:new(list_to_atom("_ets_table_" ++ integer_to_list(I)),
          [public, named_table])
  || I <- lists:seq(1, 1750) ],
ets:insert('_ets_table_1', {v1, v2, v3}).
```
You can open the Tools -> Your node -> Table Visualizer and see the ETS tables

Atoms and ETS doesn't implement Garbage Collector. You can stop the process

4. Process Limit

Erlang process by default: 32,768
```
Shell = self().

[ spawn(fun()-> receive after 120000 -> Shell ! I end end) || I <- lists:seq(1, 30147) ].
```

If your system have different limit
```
ProcessLimit = try erlang:system_info(process_limit) of
        Limit -> round(Limit * 0.92)
    catch
        error:badarg -> round(32768 * 0.92)
    end.

Shell = self().

[ spawn(fun()-> receive after 120000 -> Shell ! I end end) || I <- lists:seq(1, ProcessLimit) ].
```

Alarm: process_limit_major && process_message_queue_major

## Learning more

To find out more about memory and system limits, see the following official Erlang documentation: http://www.erlang.org/doc/efficiency_guide/advanced.html

## Log Entries

In the node you are running, enter the following:

> error_logger:error_msg("My error").

You will see the error_logger notification in the list of notifications for your node.

Go to Live Metrics, select Process notifications, and then select the Busy port, Large heap and Long schedule notifications.

## Mnesia from Learning Erlang Programming

- Packages as an OTP application
- To use:
    + Create an schema (you can use as a ram only db)
    + Start Mnesia
    + Create tables
    + Manipulate your data
- Schema: 
    + Collection of table definitions that describe your database
    + Covers which tables are stored on ram or disk, differ from node to node

- Distributed Mnesia
    + Create schema when then nodes are connected `mnesia:create_schema([node()|nodes()]).`
    + If you aren't using a distributed enviroment only pass `[node()]` as arg
    + will propagate to the other nodes automatically
    + Each node will create a directory `erl -mnesia dir Dir`

- Starting Mnesia
    + `application:start(mnesia).` or `mnesia:start().`
    + If you start Mnesia without a schema, a memory-only database will be created.
    + Stop `application:stop(mnesia)` or `mnesia:stop()`

- Mnesia Tables
    + Contains Erlang records
    + `mnesia:create_table(Name, Options)`
    + Each instance of a record in a Mnesia table is called an object.

### Meeting with Francesco and Ali

- How Wombat reacts in the Mnesia Partition
- Wombat Agent
- Add elixir examples
- Netslip in circle ci
- Trigger mnesia backups
- See how to backup 
- Visuailzation of the wombat

TO DO

- Get exposure to Erlang getting Mnesia up and running on docker, and simulate a network partition. 
- Upgrade training material. (including QLC). 
- Add sections to training material on how to use Mnesia with Docker & K8, disaster recovery from backup, and examples on tracing levels. 
- Expan operations module. 
- With Francesco, draw diagram on using dirty reads with the risk of inconsistent data as a result. 
- Show how to serialise operations in a process. 

- Explore the Wombat Mnesia plugin, and make sure we have all the metrics. 
- See if we can trigger backups, reload them. 
- Review trace data. Improve. 
- Assess the metrics already present for mnesia in Wombat.
- Advise on additional ones that can be included.
- Test the “Recover from partitioned mnesia tool” and advise on usability.
- Advise on additional OAM features that we could add to Wombat.
- Advise on Visualisation/UX improvements in Wombat.

Flows for slides

1. Mnesia Network partition using docker
    + Create docker network
    + Connect two nodes with mnesia 
2. Add a new node in Wombat
    + Topology
    + Metrics
    + Logs
    + Alarms
    + Tools
3. Explore a mnesia node in wombat: agent and table visualizer
4. Wombat and Mnesia
    + Node Down alarm
    + Network nodes: add second node
    + Add Mnesia table and records and make dirty reads
    + Disconnect one node and get a inconsistent_database alarm
    + Recover from partitioned mnesia

The following Items and Values are most commonly used:
- {disc_copies, Nodelist} Provides the list of nodes where you want disc and RAM replicas of the table.
- {disc_only_copies, Nodelist} Nodelist contains the nodes where you want disc-only copies of this particular table. This is usually a backup node, as local reads will be slow on these nodes.
- {ram_copies, Nodelist} Specifies which nodes you want to have duplicate RAM copies of this particular table. The default value of this attribute is [node()], so omitting it will create a local Mnesia RAM copy.
- {type, Type} States whether the table is a set, ordered_set, or bag. The default value is set.
- {attributes, AtomList} Is a list of atoms denoting the record field names. They are mainly used when indexing or using query list comprehensions. Please, do not hardcode them; generate them using the function call record_info(fields, RecordName).
- {index, List} Is a list of attributes (record field names) which can be used as secondary keys when accessing elements in the table.

```
2> Fields = [msisdn,id,status,plan,services].
[msisdn,id,status,plan,services]

mnesia:create_table(usr, [{disc_copies, [node()]},
{ram_copies, nodes()}, {type, set}, {attributes, Fields}, {index, [id]}]).
```

- When starting the Mnesia application, all tables configured in the schema are created or opened. This is a relatively fast, nonblocking operation, done in parallel with the startup of other applications.
- For large persistent tables, or tables that were incorrectly closed and whose backup files need repair, other applications might try to access the table, for avoid this `mnesia:wait_for_tables(TableList, TimeOut)` where TableList is the table names and timeOut is the atom `infinity`

```
-module(usr).
-export([create_tables/0, ensure_loaded/0]).
-export([add_usr/3, delete_usr/1, set_service/3, set_status/2,
delete_disabled/0, lookup_id/1]).
-export([lookup_msisdn/1, service_flag/2]).
-include("usr.hrl").

%% Mnesia API
create_tables() ->
    mnesia:create_table(usr, 
                        [
                            {disc_copies, [node()]}, 
                            {ram_copies, nodes()},
                            {type, set}, 
                            {attributes,record_info(fields, usr)},
                            {index, [id]}
                        ]).
ensure_loaded() ->
    ok = mnesia:wait_for_tables([usr], 60000).
```

## Transactions

- As many concurrent processes, possibly located on different nodes, can access and manipulate objects at the same time, you need to protect the data from race conditions.
- A transaction: 
    + guarantees that the database will be taken from one consistent state
to another
    + changes are persistent and atomic across all nodes
    + transactions running in parallel will not interfere with each other
- Encapsulate the operations in   a fun and executing them in a transacion `mnesia:transaction(Fun)`, the fun contains operations such as read, write, and delete.
- When executing your fun in a transaction, Mnesia will put locks on the objects it has to manipulate. If another process is holding a conflicting lock on an object, the transaction will first release all of its current locks and then restart.

## Writting 

1. use the function mnesia:write(Record)
2. encapsulating it in a fun
3. executing it in a transaction

Mnesia will put a write lock on all of the copies of this object (including those on remote nodes).

## Reading and deleting

- To read objects, you use the function mnesia:read(OId), where OId is an object identifier of the format {TableName, Key}.
- You need to execute the function within the scope of a transaction; failing to do so will cause a runtime error.
- Note from which node we are now reading the record. It does not make a difference.

```
(switch@Vaio)5> mnesia:read({usr, 700000003}).
** exception exit: {aborted,no_transaction}
in function mnesia:abort/1
```

## Indexing

- When creating the usr table, one of the options we passed into the call was the tuple `{index, AttributeList}`
- allowing us to look up and manipulate objects using any of the secondary fields (or keys) listed in the AttributeList
- For use it `index_read(TableName, SecondaryKey, Attribute).`

## Dirty Operations

- Execute an operation outside the scope of a transaction without setting any locks.
- dirty operations are about 10 times faster than their counterparts that are executed in transactions
- dirty operations will significantly enhance the performance of your program

```
dirty_read(Oid)
dirty_write(Object)
dirty_delete(ObjectId)
dirty_index_read(Table, SecondaryKey, Attribute)
```

- transactions quickly become a major bottleneck in some cases
- A common way to use dirty operations while ensuring data consistency is to serialize all destructive operations in a single process.
- If you need to use dirty operations in a distributed environment, the trick is to ensure that updates to a certain key subset are serialized through a process on a single node.

## Inconsistent Tables

- Using dirty write on two nodes
- Add a record in two nodes when they're disconnected
- Reconnect both nodes through TCP/IP connection
- Both entries gets buffered on both nodes
- This will generate race condition and overwriting the entry in the peer node
- With transactions this would not have occurred

## Partitioned Networks

- One biggest problem in a distributed environment is the partitioned network

Asumme: 
    1. Two erlang nodes with mnesia table
    2. Network glitch occurs
    3. Both copies of the table are updated independtly 
    4. The network comes back
    5. You have an inconsistent shared table
    6. Mnesia will know the tables are partitioned and will report
    7. What do you?

### Set master nodes

> mnesia:set_master_nodes(Table, Nodes).

- Mnesia will take the content of the master node and will duplicated in the partitioned nodes
- As soon as you increase the number of replicas in tghe nodes you will have more risk of partitioned network
- It's important have a recovery plan from partitioned databases 

## Monitoring and Preemptive Support

- your secret sauce to high availability is achieving a high level of
visibility into what is going on in your system and the ability to act on the information you collect
- will use all this information for two purposes: preemptive support
and postmortem debugging.
- Monitoring the system will allow them to pick up
early warning signs and address problems before they get out of control
- If you do not have snapshots of the system, debugging will be not be methodical and you will have to rely on guesswork
- Ensuring you have the visibility and historical data will be time well spent prior to launch

## Monitoring

- Without proper visibility in place, you can only guess the current state of
your system and are unable to spot trends and address issues before they escalate
- What thing cause the crash?
- systems need to be monitored, and information
stored for later access.

Usages:
    - Logs: record state changes in your program
    - Metrics: Polling a value at a particular point in time
    - Alarms: Event associated with a state

### Monitoring + Configuration + Management = Operation, Administration and Maintennance OAM

- All systems should let you inspect, manage, and do basic troubleshooting
- This OAM functionality have his own node
- OAM nodes can be used to handle both Erlang and non-Erlang components of your
software.
- monitor and manage your network, switches, load balancers, firewalls, hardware, OS, and stack

### Logs

- A log is an entry in a file or database that records an event that can be used as part of an audit trail
- variety of purposes, including tracing, debugging, auditing, compliance monitoring, and billing.
- have logs that allow those using them to uniquely follow the flow of
requests across nodes in order to locate issues or gather required data
- SASL logs for OTP
- If you want high availability, you need to automate the discovery of the SASL crash and error reports, and then ensure any faults get addressed.
- Think about what will give the maintainers, support engineers, DevOps
team, accountants, auditors, marketing, and customer service representatives a good overview of what is happening or has happened. Every time a notable change in state occurs, log useful information that was not previously stored
- Replaying the state transitions in the FSM would allow DevOps engineers to
retrace the steps taken by users adding items to their shopping baskets and paying for them.
- As a minimum requirement, always log the incoming and outgoing requests and results where appropriate so you are later able to identify the problematic system or component.
- Always log all Erlang shell commands and interactions
- Other items to log could include network connectivity and memory issues, which are notifications arising from the system_monitor
- “a database is a cache of your event logs,” if your database (or state) gets corrupted, the logs should tell you why

## Metrics

-  Metrics are sets of numeric data collected at regular intervals and organized in chronological order.
-  You need to retrieve data on the OS and network layers, on the middleware layer
- Improve the performance and reliability of the system and troubleshoot issues after they have occurred
- monitor the system to detect abnormal behavior and prevent failures
- predict trends and usage spikes, using the results to optimize hardware costs
- study long-term user trends and user experience
- make sure the system load doesn’t exceed available resources, requesting metrics on the memory usage of the Erlang VM.
- One typical value is an amount, a discrete or continuous value with incremental and decremental capabilities. 
- A common form of amount is counters, as we have seen.
- Gauges are a form of counter that provide a value at a particular point in time.

Measures:
    - Memory
    - Time (latency) for generate histograms

1. Amount
    - Counters
2. Gauges 
    - Memory management  
    - Histograms
3. Meters
    - Spiral
    
### Alarms

- Alarms are a subset of events associated with a state.
- While an event will tell you that something happened, an alarm will indicate that something is ongoing.
- An alarm is raised when the issue you are monitoring manifests itself.
- The alarm is said to remain active until the issue is resolved
- Alarms can also be associated with a severity. Severities include cleared, indeterminate, critical, major, minor, and warning.
- Alarms can originate from the affected node or in the OAM node itself. They can be based on thresholds or state changes, or a mixture of the two.
- In threshold-based alarms, metrics are monitored and the alarm is raised if a limit is exceeded in one of the metrics.

### Preemptive Support

- Support automation is the building of a knowledge base that is used to reduce service disruption by reacting to external stimuli and resolving problems before they escalate.
- downtime is something you need to plan for when designing your system.
- Automation is achieved through the collection and analysis of metrics, events, alarms, and configuration data.
- preemptively trying to resolve the problem before it occurs.

Keep in mind
1. Proactive support automation is focused on reducing downtime using ent to end health checks and diagnostic procedures
2. Preemptive support automation gathers data as metrics, events, alarms and logs and use the results to predict service disruptions before they occur
3. Self support automation describes the tools and libraries that can be used to troubleshoot solutions and to diagnose and resolve problems

 Conclusion:

1. Split up your system’s functionality into manageable, standalone nodes.
2. Choose a distributed architectural pattern.
3. Choose the network protocols your nodes, node families, and clusters will use when
communicating with each other.
4. Define your node interfaces, state, and data model.
5. For every interface function in your nodes, pick a retry strategy.
6. For all your data and state, pick your sharing strategy across node families, clusters,
and types, taking into consideration the needs of your retry strategy.
7. Design your system blueprint, looking at node ratios for scaling up and down.
8. Identify where to apply backpressure and load regulation.
9. Define your OAM approach, defining system and business alarms, logs, and metrics.
10. Identify where to apply support automation.




Advicing Wombat

- Docker network
- Wombat phylosopy: blog post
- Wombat installation
- Adding a simple node in wombat
    - Add node
    - Topology
    - Metrics
    - Logs
    - Alarms
    - Tools
- Add node with mnesia
    - Metrics

