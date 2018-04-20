
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
    we can user global to explicitly treat the variable as global variable 
    in spite of the assignment within the function.

## Closures
    closures only matter when you have nested functions 
    (that you need to deal with external variables that are no-global)
    closure is function with an extended scope that 
    encompasses no-global variables (free variables) 
    referenced in the body of the function but not defined there.


## Decorators in the standard library
### functools.wraps
    copy the relevant attributes from decorated func to wrapper func
    
### functools.lru_cache
    save the previous invocation of an expensive function
    least recently used
    
### functools.singledispatch
    if you decorate a plain function with @singledispatch, 
    it becomes a generic function: a group of functions to perform the same operation in different ways, 
    depending on the type of the first argument
    
### Parametrized Decorators
    make adecorator factory that takes those arguments and returns a decorator

# Dynamic attributes and properties
## coding 
    from urllib.request import urlopen
    
    with open(a, 'w') as f1, open(b, 'w') as f2:
    
    __getattr__ is called only when there's no attribute with that name
    __getattribute__ is called all the times for all kind of attributes
    
    an alternate constructor is using @classmethod decorator
    
## Class constructor
    an alternate constructor is using @classmethod decorator
    __new__ is a special classmethod without the decorator
    The path just described, from __new__ to __init__ is the usual, but not the only one.
    The __new__ method can also return an instance of a different class, and when that
    happens, the interpreter does not call __init__.
    
## Property
    properties are alwyas class attributes, but they actually manage attribute access in the instances of the class
    instance attribute shadow class attribute, but does not shadow class property
    obj.attr does not search for attr starting with obj. it starts at obj.__class__. 
    If there is no property named attr in the class, python looks in the obj instance itself.
