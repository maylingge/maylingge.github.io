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
