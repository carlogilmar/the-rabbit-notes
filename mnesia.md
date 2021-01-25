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
