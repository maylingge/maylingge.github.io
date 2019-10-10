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

# Django n+1 issue detector
     > /home/lynn/.local/lib/python2.7/site-packages/nplusone/core/listeners.py(101)handle_lazy()
     -> model, instance, field = parser(args, kwargs, context)
     (Pdb) bt
       /usr/lib/python2.7/threading.py(774)__bootstrap()
     -> self.__bootstrap_inner()
       /usr/lib/python2.7/threading.py(801)__bootstrap_inner()
     -> self.run()
       /usr/lib/python2.7/threading.py(754)run()
     -> self.__target(*self.__args, **self.__kwargs)
       /usr/lib/python2.7/SocketServer.py(596)process_request_thread()
     -> self.finish_request(request, client_address)
       /usr/lib/python2.7/SocketServer.py(331)finish_request()
     -> self.RequestHandlerClass(request, client_address, self)
       /home/lynn/.local/lib/python2.7/site-packages/django/core/servers/basehttp.py(102)__init__()
     -> super(WSGIRequestHandler, self).__init__(*args, **kwargs)
       /usr/lib/python2.7/SocketServer.py(652)__init__()
     -> self.handle()
       /home/lynn/.local/lib/python2.7/site-packages/django/core/servers/basehttp.py(182)handle()
     -> handler.run(self.server.get_app())
       /usr/lib/python2.7/wsgiref/handlers.py(85)run()
     -> self.result = application(self.environ, self.start_response)
       /home/lynn/.local/lib/python2.7/site-packages/django/contrib/staticfiles/handlers.py(63)__call__()
     -> return self.application(environ, start_response)
       /home/lynn/.local/lib/python2.7/site-packages/django/core/handlers/wsgi.py(189)__call__()
     -> response = self.get_response(request)
       /home/lynn/.local/lib/python2.7/site-packages/django/core/handlers/base.py(132)get_response()
     -> response = wrapped_callback(request, *callback_args, **callback_kwargs)
       /home/lynn/projects/django-projects/mysite/polls/views.py(16)index()
     -> if cm.owner:
       /home/lynn/.local/lib/python2.7/site-packages/nplusone/core/signals.py(23)wrapped()
     -> ret = func(*args, **kwargs)
       /home/lynn/.local/lib/python2.7/site-packages/django/db/models/fields/related.py(602)__get__()
     -> rel_obj = qs.get()
       /home/lynn/.local/lib/python2.7/site-packages/nplusone/core/signals.py(23)wrapped()
     -> ret = func(*args, **kwargs)
       /home/lynn/.local/lib/python2.7/site-packages/django/db/models/query.py(328)get()
     -> num = len(clone)
       /home/lynn/.local/lib/python2.7/site-packages/django/db/models/query.py(144)__len__()
     -> self._fetch_all()
       /home/lynn/.local/lib/python2.7/site-packages/nplusone/ext/django/patch.py(79)wrapped()
     -> parser=parser,
       /home/lynn/.local/lib/python2.7/site-packages/blinker/base.py(267)send()
     -> for receiver in self.receivers_for(sender)]
     > /home/lynn/.local/lib/python2.7/site-packages/nplusone/core/listeners.py(101)handle_lazy()
     -> model, instance, field = parser(args, kwargs, context)
