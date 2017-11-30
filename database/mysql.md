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
    
    A given character set always has at least one collation, and most character sets have several. 
    show collation;
    
    If your character set index file does not contain the name for the character set, your program displays an error message. The file is     named Index.xml and the message is:

    Character set 'charset_name' is not a compiled character set and is not
    specified in the '/usr/share/mysql/charsets/Index.xml' file
    To solve this problem, you should either get a new index file or manually add the name of any missing character sets to the current file.



# VARCHAR 
    alter table test modify name varchar(2000);
    
    failed with following error:
    	
        This question already has an answer here:
        #1071 - Specified key was too long; max key length is 1000 bytes 
        
    This is because we have index on field 'name'.
    And MyISAM has a limit of 1000 bytes for indexes.InnoDB has an even smaller limit (767 bytes) unless you're on MySQL 5.7.7+, in which case the limit is 3072 bytes by default.
    drop the index or try to reduce your index size. Such as using prefix as index

# MySQL Collation
    each character set has a default collation
    
## Server level
    default is latin1 and latin1_swedish_ci
    to change the default server setting, you need to recompile MySQL source code.
    
## Database level
    To change database default character set and collation:
        Alter database db_name CHARACTER SET latin1 COLLATE latin1_swedish_ci;
    To see the default character set and collation for a given database:
        USE db_name; SELECT @@character_set_database, @@collation_database;
    can only affect the newly created table;
 
## Table level
    The table character set and collation are used as default values for column definitions if the column character set and collation are not specified in individual column definitions. The table character set and collation are MySQL extensions; there are no such things in standard SQL.
    CREATE TABLE t1
    (
        col1 CHAR(10)
    ) CHARACTER SET latin1 COLLATE latin1_bin;

## Column level
    ALTER TABLE t1 MODIFY
    col1 VARCHAR(5)
      CHARACTER SET latin1
      COLLATE latin1_swedish_ci;
    


# Variables
    MySQL has three different kinds of variables: local variable, session variable, global variable
    session is created when a client is connected with the server and terminated when the connection closed.
    select @@variable_name; # global/session variable
    select @variable_name; # local variable
    
    show [global|session] variables like 'pattern'| where expr;

