## Partitioned Network in a Docker erlang cluster


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
