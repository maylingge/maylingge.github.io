
# memory leak in Python
It’s not so easy for a Python application to leak memory. Usually there are three scenarios:

some low level C library is leaking
your Python code have global lists or dicts that grow over time, and you forgot to remove the objects after use
there are some reference cycles in your app
