# Transaction
use autocommit by default, each query is executed in its own transaction
autocommit may not be a good choice for innodb

_Each query is immediately committed to the database, unless a transaction is active_


# how to install django_wsgiserver with pyopenssl
   pip install pyopenssl==0.13
   pip install django_wsgiserver
   
   cp OpenSSL/SSL.so OpenSSL.SSL.so
   cp OpenSSL/rand.so OpenSSL.rand.so
   cp OpenSSL/crypto.so OpenSSL.crypto.so
