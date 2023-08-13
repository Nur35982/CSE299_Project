from django.contrib import admin
from Auth.models import Volunteer

# Register your models here.
class VolunteerAdmin(admin.ModelAdmin):
    list_display=('id', 'vid', 'vname', 'vemail')
admin.site.register(Volunteer,VolunteerAdmin)