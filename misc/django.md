# Transaction
use autocommit by default, each query is executed in its own transaction
autocommit may not be a good choice for innodb

_Each query is immediately committed to the database, unless a transaction is active_