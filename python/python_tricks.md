## Assert statement
    can be disabled by an intepreter setting
    not for data validation
    but to catch impossible conditon and raise exception under debug mode
    
    how to disable/enable under freeze?
    same as python intepreter

    __debug__
        True if python is not started with -O, -OO
        sys.flags.debug

    PYTHONOPTIMIZE
        sys.flags.optimize  0,1,2

## Context manager (with statement)
    class-based 
        return
    @contextmanager-based
        yield
    
## name mangling
    __var
    _Classname_var
    
## import *
    __all__
    

## python namespaces
    __builtins__
    LEGB : local enclosing global builtins
    
## Function
  ### Functions are first-class
    inner function can capture and cary some of the parent function's state
    A closure remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.
    all functions are objects in Python and object can also act as a function to be callable
    built-in function "callable" to check whether an object is callable.
    
  ### closure
    non-local variables are in the enclosing scope
    __closure__ is only available when non-local variables are used in the inner function
    
    __closure__[0].cell_contents
  
  ### method
    method is a function which belongs to an object and can access the associated data of that object.
   
  ### decorators
    def mydec(func):
        @functools.wraps(func)            # carries over the docstring and other metadata of the input function
        def wrapper(*args, **kwargs)      # store all positional arguments in args, and keyword arguments in kwargs
            return_value = func(*args, **kwargs) # unpack the arguments to input function
            return return_value
        return wrapper
  ### return None : implicitly
  
  
## Classes
  ### every class needs a __repr__
  ### exception
     define your own exception class and define your own base exception class
  ### clone
     shallow copy is just one level deep
     import copy
     # shallow
     copy.copy
     
     for built-in collections, just use list,dict and set factory functions to create shallow copies
     # deep
     copy.deepcopy
     
     define __copy__() and __deepcopy__() to customize the copy behavior
  
## Others
### code linter
    pylint
    
### freeze
    python freeze.py test.py
    make
    
### print statement in 2.x and print function in 3.x

### PEP8
