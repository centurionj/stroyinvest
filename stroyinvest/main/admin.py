from django.contrib import admin
from django.contrib.auth.models import Group, User

admin.site.site_header = 'ООО «СТРОЙИНВЕСТ»'
admin.site.site_title = 'ООО «СТРОЙИНВЕСТ»'
admin.site.index_title = 'ООО «СТРОЙИНВЕСТ»'

admin.site.unregister(User)
admin.site.unregister(Group)
