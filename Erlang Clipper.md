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

## Getting Started Guide


