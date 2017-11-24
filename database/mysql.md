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



# String comparison 
    case sensitive or insensitive
    Whenever you create database in MySQL, the database/schema has a character set and a collation. Each character set has a default collation; see here for more information.
    The default collation for character set latin1, which is latin1_swedish_ci, happens to be case-insensitive.
    You can choose a case-sensitive collation, for example latin1_general_cs (MySQL grammar):
  [how to do a case sensitive search in mysql](https://dba.stackexchange.com/questions/15250/how-to-do-a-case-sensitive-search-in-where-clause)
    
    how to choose the proper character set and collation
    
  [mysql character set](https://dev.mysql.com/doc/refman/5.7/en/charset.html)
  
    A character set is a set of symbols and encodings. 
    A collation is a set of rules for comparing characters in a character set. 
    
  select * from information_schema.character_sets;
  show character set like 'latin%';
