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
    
    
## Others
### code linter
    pylint
    
### freeze
    python freeze.py test.py
    make
    
### print statement in 2.x and print function in 3.x
