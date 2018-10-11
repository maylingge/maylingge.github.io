
# memory leak in Python
It’s not so easy for a Python application to leak memory. Usually there are three scenarios:

some low level C library is leaking

your Python code have global lists or dicts that grow over time, and you forgot to remove the objects after use

there are some reference cycles in your app

# memory monitor in Python
## monitor memory usage per line
    memory_profiler:
    install:
      pip install -U memory_profiler
    
    usage:
      from memory_profiler import profile
      add @profile on the function that you want to monitor
      
    example:
    @profile
    def my_func():
        a = [1] * (10 ** 6)
        b = [2] * (2 * 10 ** 7)
        del b
        return a

    if __name__ == '__main__':
        my_func()

## monitor memory usage in heap
    http://smira.ru/wp-content/uploads/2011/08/heapy.html
    guppy:
    install:
      pip install guppy
      
    usage:
      from guppy import hpy
      hy = hpy()
      heap = hy.heap()
      # check the referrer
      hy.heap()[0].byrcs
      
      # check all the items referenced by the first referrer
      hy.heap()[0].byrcs[0].byid
      
      # check one of the item
      hy.heap()[0].byrcs[0].byid[0].theone
      
      # check the type of the referenced items by the first referrer
      hy.heap()[1].byrcs[0].byclodo 
      
      hp.setrelheap()  # Everything allocated before this call will not be in the data sets you get later. reset
      
      
