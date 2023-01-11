# Mnesia

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

---

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

### Mnesia Metrics

- Mnesia Info `mnesia:system_info(all).`

> https://erlang.org/doc/man/mnesia.html#system_info-1

Options as atoms:
- all
- access_module
- auto_repair
- backup_module
- checkpoints
- event_module
- db_nodes
- debug
- directory
- dump_log_load_regulation
- dump_log_update_in_place
- dump_log_write_threshold
- extra_db_nodes
- fallback_activated
- held_locks
- is_running
- local_tables
- lock_queue
- log_version
- master_node_tables
- protocol_version
- running_db_nodes
- schema_location
- subscribers
- tables
- transactions
- transaction_failures
- transaction_commits
- transaction_restarts
- transaction_log_writes
- use_dir
- version

### Mnesia System information

> http://erlang.org/documentation/doc-5.0.1/lib/mnesia-3.9.2/doc/html/Mnesia_chap7.html

Retrieve system information:
- `mnesia:table_info`
- `mnesia:system_info`

- If Mnesia malfunctions, system information is dumped to a file named  `MMnesiaCore.Node.When.`
- If a Mnesia system behaves strangely, it is recommended that a Mnesia core dump file be included in the bug report. `mnesia_lib:coredump().`

- The table content is placed in a .DAT file on the disc. When the Mnesia system is started, the RAM table will initially be loaded with data from its .DAT file.

# Restore Database

- Create schema `mnesia:create_schema([node()]).`
- Start Mnesia `mnesia:start().`
- Create record `rd(user, {username, code})`
- Create table stored in disc not in ram `mnesia:create_table(user, [{disc_copies, [node()]}]).` 
- Add some records and delete 

```
[ mnesia:transaction(fun() -> mnesia:write({user, list_to_atom(io_lib:format("user~B", [Idx])), Idx}) end) || Idx <- lists:seq(1, 10)].
```

```
mnesia:dirty_delete(user, user1).
mnesia:dirty_delete(user, user5).
mnesia:dirty_delete(user, user10).
```

- Make the backup `mnesia:backup("backup.bup").`
- Add more records
```
[ mnesia:transaction(fun() -> mnesia:write({user, list_to_atom(io_lib:format("user~B", [Idx])), Idx}) end) || Idx <- lists:seq(1, 100)].
```
- Restone table
```
mnesia:restore("backup.bup", [{default_op, clear_tables}]).
```
