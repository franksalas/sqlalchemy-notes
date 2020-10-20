# Intro to SQLAlchemy

SQLAlchemy is a python library used to iteract with a wide variety of databases.  It enables you to create data models & queries in a manner that feels like a normal Python chasses and statements. Created by Mike Bayer in 2005, it is consider by many to be the de facto way of workng with relationa databases in Python.

## Why use SQLAlchemy

To abstract your code away from underlying database and its associated SQL peculiarities.IT helps ensue that database input is sanitized and properly escaped pritot obeign submitted ti the database. This prevents common issues like SQL injectoin atacks.

SQLAlchemy provides a lot of flexibility by supplying twi major modes or usage
- SQL Expression Language also known as $Core$
- $ORM$

## $CORE$
The SQL Expression Language is a pythonic way of representing common SQL statements and expressions. It also acts as the foundation for the SQLAlchemy ORM

## $ORM$
The SQLAlchemy ORM is simmilar to many other object reletional mappers (ORMs), Its focused around the domain model of the application and leverages the Unit of Work pattern to maintatin obhect state.

## Core vs ORM
The two modes use slightly diffrent syntax, but the biggest difference between Core & ORM is the view of dat as chemoa or business objects..
### CORE
  - schema-centric view
  - traditional sql , tables, keys, index structure
  - data warehouse
  - reporting
  - analysis
  - scenarieos where beign able to tightly control the query or operating on unmodeled data .

The STron database connection pool and result-set optimizations are perfectly suited to deal with large amounts of data, even in multiple databases.

### ORM
-  domain-driven design
-  encapsulate much of the underlying schema & structure in metadata & business objects
-  easy to make databse interactions feel like normal python code.
-  highly effective way to inject domain-driven design  into a legacy app
-  microservices

### Checklist
- If you are working with a framework that already has an ORM built in, but want
to add more powerful reporting, use Core.

- asdf
- If you want to view your data in a more schema-centric view (as used in SQL),
use Core
- If you have data for which business objects are not needed, use Core.
- If you view your data as business objects, use ORM.
- If you are building a quick prototype, use ORM.
- If you have a combination of needs that really could leverage both business
objects and other data unrelated to the problem domain, use both!
![](https://tekshinobi.com/wp-content/uploads/2020/04/box-diag-sqla.jpg)
## Terms

## CORE Terms
- Engine: a registry which provides connectivity to a particular database server.
-  dialect: Intreprets generic SQL and database commands in terms of a specific DBAPI and database backend
-  connection pool: hold a collection of database connection sin memory for fast re-use.
-  SQL Expression Language: Allows SQL statements to be written using Pyhton expressions.
-  Schema/Types: USes Python objects to represent tables, columns, and datatypes.

## ORM TERMS
- allows construction of Python objects whick can be mapped to relational database tables
- Transparently persisit objects into their corresponding databse tables using the **unit of work** pattern 
- provides a query system  whick loads obkects and attribuetes using SQL generated from mappings.
- buids on top of the Core- uses the Core to generate SQL  and talk to the databse.

##
-------------------------------------
- https://www.youtube.com/watch?v=woKYyhLCcnU&t=1567s&ab_channel=NextDayVideo


![](https://tekshinobi.com/wp-content/uploads/2020/04/onion-diag-sqla.jpg)


# Level 1: Engine, Connection, Transactions
## Python DBAPI
- De-facto sytem for providing Python database interfaces
- Many DBAPI implementations available, most databases habe more that one.

### Important DBAPI FActs
- DBAPI assumes that transaction is alwasy in progrsss. There is no `begin()` method, ony `commit()` and `rollback()`
- DBAPI encourages bound parameters, via the `execute()` and `executemany() methods. But has six diffrent formats
- All DBAPIs habe inconsitencies regarding datatypes, primary key generation, custom database features, result/cursor behavior
- DBAPI has it's own exeption hierarchy, whic SQLAchemy exposes directly

## SQLAlchemy and the DBAPI
- The fist layer in SQLAlchemy is knowna sthe **Engine**, which is the object that maintains the classical DBAPI interaction.


------------------
# Engine Facts
- executing via the Engine directly is called **connectionless execution** - the engine connects and disconnects for us.
- Using a Connection is called **explicit exectution**. we control the span of a connection in  use.
- Engine usially uses a connection pool, which means "disconnecting" often means the connection is just returned to the pool.
- The SQL we send to the `engine.execute()` as a string is not modified, is consimed by the DBAPI verbatim.
- 
--------------------------------------
# Level 2: Table, metadata, reflection, DDL

## What is metadata?
- describes the structure of the database, tables, columns, constraints, in terms of data structres in python
- servs a s the basis for SQL generation and object releational mapping
- can genrate *to* a schema
- can be generated *from* a schema
- 