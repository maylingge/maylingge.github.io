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
    
## Function
  ### Functions are first-class
    inner function can capture and cary some of the parent function's state
    A closure remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.
    all functions are objects in Python and object can also act as a function to be callable
    built-in function "callable" to check whether an object is callable.
    
## Others
### code linter
    pylint
    
### freeze
    python freeze.py test.py
    make
    
### print statement in 2.x and print function in 3.x

### PEP8
