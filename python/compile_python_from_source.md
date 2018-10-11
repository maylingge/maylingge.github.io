# compile python with valgrind support
    ./configure --prefix /tmp/python_dbg --with-threads --with-pydebug --without-pymalloc --with-valgrind
    make
    make install
    
    "UNREF invalid object" 
    this kind of error is due to inconsistent python libraries from different version(build).
    
    prefer to run the compilation on a physical machine which has gcc, valgrind and openssl installed in the default localtion.
