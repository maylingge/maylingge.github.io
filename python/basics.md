# iter()
  iteration protocol: 
  
  __iter__()  : proxy to another iterator
  
  sequence protocol: __getitem__()
  
  ## iterable
  
    An object capable of returning its members one at a time. 
    Examples of iterables include all sequence types (such as list, str, and tuple) 
    and some non-sequence types like dict and file and objects of any classes you define with an *__iter__()* or *__getitem__()* method. 
    Iterables can be used in a for loop and in many other places where a sequence is needed (zip(), map(), ...). 
    When an iterable object is passed as an argument to the built-in function iter(), it returns an iterator for the object. 
    This iterator is good for one pass over the set of values. 
    When using iterables, it is usually not necessary to call iter() or deal with iterator objects yourself. 
    *The for statement does that automatically for you, creating a temporary unnamed variable* to hold the iterator for the duration of the loop. 
    
    
  ## iterator
  must support:
    __iter__()
    
    next()
    
    An object representing a stream of data. 
    Repeated calls to the iterator’s next() method return successive items in the stream. 
    When no more data are available a StopIteration exception is raised instead. 
    At this point, the iterator object is exhausted and any further calls to its next() method just raise StopIteration again. 
    Iterators are required to have an *__iter__()* method that returns the iterator object itself so every iterator is also iterable and may be used in most places where other iterables are accepted. 
    *One notable exception is code which attempts multiple iteration passes. *
    *A container object* (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop. 
    Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.
    

https://docs.python.org/2/library/stdtypes.html#typeiter


# generator & yield

## a generator is a special type of iterator

## yield a value when a value sent to me
def get_primes(number):

     while True:
         if is_prime(number):
            number = yield number
        number += 1
        
https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

# enumerate()

# next(iterator[, default]) 
    raise StopIteration or return default
    
    
# re
    metacharacters: . * + ^ $ ? \ | [ ] { } ( ) 
    [abc]  [a-c]: a set of characters  . Metacharacters are treated as normal ones inside classes. [^a-c]: for charaters not in the set
    \ : the backslash can be followed by various characters to signal various special sequences. to remove the special meaning
        \d
        \D
        \w
        \W
        \s any spaces
        \S
        
     . : it matches anything except a newline. if re.DOTALL specified, it will match anything
     
     repeating:
     {m,n}
     * {1,}
     ? {0, 1}
     + {1,}
     
     Regular expressions are compiled into _pattern objects_
     
     preferred to write regular expression in python raw string: r'\n' to handle backslash properly.
     
     _match object_
    
    
