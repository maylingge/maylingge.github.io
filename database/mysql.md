# Lock

## [a-few-notes-on-locking-in-mysql](http://www.ovaistariq.net/612/a-few-notes-on-locking-in-mysql/#.WRGaSfmGO70 )
### shared lock (read lock)
### exclusive lock (write lock)

### myisam
table level locking
concurrent insert is also supported

### innodb
transaction

row level locking

some field still requires table level locking (such as auto_incr field)





## [table locking issue in mysql](https://dev.mysql.com/doc/refman/5.7/en/table-locking.html)
### give select higher priority
### concurrent insert of myisam
### max write count


# Transaction

# Isolation level

# MVCC
