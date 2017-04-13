# Design patterns in LevelDB
## DB & DBImpl
### DB::Open  
why use pointer of pointer to hold DB?
 To pass out the DBImpl through input parameter
 
 
### DBImpl::Write
log_->AddRecord
WriteBatchInternal::InsertInto


### DBImpl::MaybeScheduleCompaction

# Basic operations
## WriteBatch
  MemTableInserter
  MemTable::Get
  MemTable::Add
  
  SkipList<const char*, KeyComparator> Insert

## Slice

## Put
Call writeBatch internally

## Get

## Iterator


## skiplist
### class Arena;
why need class declaration here and also <util/arena.h> is included?
no need to include arena.h here but just inside cpp file?

http://blog.marchtea.com/archives/212 
http://cighao.com/2016/08/13/leveldb-source-analysis-01-introduction/
