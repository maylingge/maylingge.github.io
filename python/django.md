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
       
                              
    
                          
                          
                        
                        
    
