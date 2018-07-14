# Django timezone
   When support for time zones is enabled, Django stores datetime information in UTC in the database, 
   uses time-zone-aware datetime objects internally,
   and translates them to the end user’s time zone in templates and forms.
   
   the datetime read from database in queryset is in UTC timezone.
   
# Where to put the util under Django project
  create a util app and registered in INSTALLED_APPS

# tastypie
