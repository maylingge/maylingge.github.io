
import time
class MeasureTime:
    def __init__(self):
        self.start = 0
        self.end = 0
    
    def __enter__(self):
        self.start = time.time()
        return
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print("Time cost: {}".format(self.end - self.start))
        
def my_func():
    time.sleep(5)
    return

with MeasureTime():
    my_func()


from contextlib import contextmanager
@contextmanager
def measureCost():
    try:
        start = time.time()
        yield
    finally:
        end = time.time()
        print("Time cost: {}".format(end - start))
