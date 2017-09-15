
- [x] re
- [x] Pyro4
- [ ] json
- [x] subprocess
- [ ] threading
- [ ] multiprocessing
- [ ] decorator
- [ ] datetime
- [ ] collections
- [ ] logging



# subprocess
[https://stackoverflow.com/questions/4417546/constantly-print-subprocess-output-while-process-is-running]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    for line in iter(process.stdout, ""):
      print line
