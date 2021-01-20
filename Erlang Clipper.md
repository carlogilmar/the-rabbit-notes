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

Learning more
To find out more about memory and system limits, see the following official Erlang documentation: http://www.erlang.org/doc/efficiency_guide/advanced.html

5. 




