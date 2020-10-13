## Assert statement
    can be disabled by an intepreter setting
    not for data validation
    but to catch impossible conditon and raise exception under debug mode
    
    how to disable/enable under freeze?

    __debug__
        True if python is not started with -O, -OO
        sys.flags.debug

    PYTHONOPTIMIZE
        sys.flags.optimize  0,1,2
    
## Others
### code linter
