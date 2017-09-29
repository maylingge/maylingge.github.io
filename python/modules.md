
- [x] re
- [x] Pyro4
- [ ] json
- [x] subprocess
- [ ] threading
- [x] multiprocessing
- [ ] decorator
- [ ] datetime
- [ ] collections
- [ ] logging
- [ ] socket 


# subprocess
## how to read output of running subprocess
[https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running]
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    for line in iter(process.stdout, ""):
      print line


# multiprocessing
    class Custom(Process):
        def __init__(self, *args, **kwargs):
            super(Custom, self).__init__()
        
        def run(self):
            os.getppid()
    
    multiprocessing.Queue: difference with Queue
    multiprocessing.Pipe: difference with subprocess.PIPE



# Logging
    threading.Lock or threading.RLock ?
    LogRecord
    Logger object
    format
    handler object
    filter object
    raiseExceptions
    https://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook
