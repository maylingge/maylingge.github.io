
# Data model
## Special methods
    83 special method names
    __str__ : for end users
    __repr__: for debuging and logging, %r, !r
    
# Data structure
## Sequence
    container sequence
    flat sequence
    
    mutable
    immutable
    
    
# Function
## first-class function
    "first-class object" can be    
    1. created at runtime
    2. assign to a variable or element in a data structure
    3. passed as an argument to a function
    4. returned as the result of a function
   
    "higher-order" function:
    a function that takes a function as argument or return a function as result
    
    seven flavors of callable objects:
    1. user defined functions
    2. built-in functions
    3. built-in methods
    4. Methods
    5. Class
    6. CLass instances
    7. Generator functions

    positional arguments & keyword arguments:
    even positional arguments can be passed as keyword but all after it must be passed in as keyword
    In python 2, we cannot define positional arguments(keyword arguments without default value) after *args
    In python 3, we can define keyword only arguments in this way:
        def func(a, *, b):
    In python 2, only **kwargs allowed after *args    
    
# Decorator
    A decorator is a callable that takes another function as argument.
    It may perform some processing with the decorated function and returns it 
    or replaces it with another function or callable object
    
    Decorators are executed immediately when a module is loaded.(import time)
    
## variable scope
    if variable is assigned within the function, it is a local variable
    we can user global to explicitly treat the variable as global variable in spite of the assignment within the function.

## Closures
    closures only matter when you have nested functions (that you need to deal with external variables that are no-global)
    closure is function with an extended scope that encompasses no-global variables (free variables) referenced in the body of the function but not defined there.


## Decorators in the standard library
### functools.wraps
    copy the relevant attributes from decorated func to wrapper func
    
### functools.lru_cache
    save the previous invocation of an expensive function
    least recently used
    
### functools.singledispatch
    if you decorate a plain function with @singledispatch, it becomes a generic function: a group of functions to perform the same operation in different ways, depending on the type of the first argument
    
### Parametrized Decorators
    make adecorator factory that takes those arguments and returns a decorator
