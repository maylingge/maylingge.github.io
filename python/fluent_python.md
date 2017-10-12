
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
    