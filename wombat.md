## Wombat OAM

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

Learning Wombat:

1. Installation
2. Adding a Node
3. Explore main information

- Home tab: Main actions over the node (evaluate erlang expression, garbage collector, recover from partition mnesia, purge old modules, terminate process, terminate shell processes)
- System: info about node name, cokkie, state, hardware, OS, Erlang VM
- Agents: agent plugins on/off

4. Node graph
5. Metrics

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

