from django.contrib import admin
from home.models import Registration
from home.models import festdesc
from home.models import *
# Register your models here.
admin.site.register(Registration)
admin.site.register(festdesc)
admin.site.register(events)
