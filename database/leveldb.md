# Design patterns in LevelDB
## DB & DBImpl
### DB::Open  
why use pointer of pointer to hold DB?
 To pass out the DBImpl through input parameter
 
 
### DBImpl::Write
log_->AddRecord
WriteBatchInternal::InsertInto

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
