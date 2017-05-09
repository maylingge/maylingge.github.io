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
### Start mysqld with a low value for the max_write_lock_count system variable to force MySQL to temporarily elevate the priority of all SELECT statements that are waiting for a table after a specific number of inserts to the table occur. This permits READ locks after a certain number of WRITE locks. 
### If you have problems with INSERT combined with SELECT, consider switching to MyISAM tables, which support concurrent SELECT and INSERT statements. (See Section 9.11.3, “Concurrent Inserts”.) 
### Start mysqld with --low-priority-updates. For storage engines that use only table-level locking (such as MyISAM, MEMORY, and MERGE), this gives all statements that update (modify) a table lower priority than SELECT statements. In this case, the second SELECT statement in the preceding scenario would execute before the UPDATE statement, and would not wait for the first SELECT to finish. 
