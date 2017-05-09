# Lock
### shared lock (read lock)
### exclusive lock (write lock)

### myisam
table level locking
concurrent insert is also supported

### innodb
transaction

row level locking

some field still requires table level locking (such as auto_incr field)

[a-few-notes-on-locking-in-mysql](http://www.ovaistariq.net/612/a-few-notes-on-locking-in-mysql/#.WRGaSfmGO70 )
