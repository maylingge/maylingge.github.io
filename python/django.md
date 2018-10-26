# Django timezone
   When support for time zones is enabled, Django stores datetime information in UTC in the database, 
   uses time-zone-aware datetime objects internally,
   and translates them to the end user’s time zone in templates and forms.
   
   the datetime read from database in queryset is in UTC timezone.
   
# Where to put the util under Django project
    create a util app and registered in INSTALLED_APPS

# tastypie
    base url and view mapping:
    /users -> dispatch_list -> obj_get_list  (overwritten function)
    /users/me -> dispatch_detail -> obj_get (overwritten function)
    
    customized url and view mapping in "prepend_urls":
    url(r'/users/me/login', self.wrap_view('login'), nam='api_login')
    'login' is the function to response to login rquest.
    
    the base url will go through the dispatch. So authentication is handled.
        def dispatch(self, request_type, request, **kwargs):
        """
        Handles the common operations (allowed HTTP method, authentication,
        throttling, method lookup) surrounding most CRUD interactions.
        """
    however, the customized url defined in "prepend_urls" is directly go the defined view.
    So prefer to define the customized view with "dispatch"


# how Django commands framework work

    django.core.management: 
    __init__.py: execute_from_command_line(sys.argv)
                 ManagementUtility.execute(argv)
                  handle general command
                  fetch_command(subcommand).run_from_argv(argv)
    
    django.core.management.Base:              
    BaseCommand: run_from_argv(argv)
                      execute(args, options.__dict__)
                        handle(args, options)
                          run(args, options)
                          inner_run(...)
                              django.core.servers.basehttp.run(addr, port, ...)
                              
    django.core.servers.basehttp
       WSGIServer(simple_server.WSGIServer)
          set_app
       WSGIRequestHandler
          run(app)
       app(env, start_response)
       
       
    django.core.handlers.wsgi
       WSGIhandler
       BaseHandler.get_response
            middleware
            view response method
       
# how to enable django debug toolbar

    1. pip install django-debug-toolbar
    2. DEBUG = True (in settings.py)
    3. put 'debug_toolbar',  into INSTALLED_APPS
    4. put 'debug_toolbar.middleware.DebugToolbarMiddleware', into MIDDLEWARE_CLASSES
    5. INTERNAL_IPS = ('127.0.0.1',) in the end of settings.py
       the ip address must be the right one, you can get the right ip through: 
       print "IP Address for debug-toolbar: " + request.META['REMOTE_ADDR']
    6. In the end of urls.py:
       if settings.DEBUG:
          import debug_toolbar
          urlpatterns += [
              url(r'^__debug__/', include(debug_toolbar.urls)),
          ]
                          
                        
# Django ORM optimize query

    .values()
    It’s useful when you only need a small number of the available fields. It's more efficient to select only the fields you need to use.
    Return a list of dict. dict is the field name/value pair.
   
    .values_list()
    similar as .values(). Return a list of tuple. Each item correspond to the field value you choose.
    if only one field is needed, such as:
    .values_list('name', flat=True)
    it returns a list of names. 
   
    .select_related()
    ForeignKey or OneToOneField relation can use this function.
    it will fetch the selected relation in one query with complex sql. avoid extra sql to query related object.
   
    db_api.raw_query()
    for more complex relationship like ManyToMany, raw sql query is better than query through Django ORM. This is the last choice only.
   
   
