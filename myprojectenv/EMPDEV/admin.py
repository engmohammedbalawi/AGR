from django.contrib import admin
from . models import *

from import_export.admin import ExportActionMixin

class publicpadmin(ExportActionMixin, admin.ModelAdmin):
         list_display = ('id', 'name')

admin.site.register(TypeDevice)
admin.site.register(TypeRamHard)
admin.site.register(Employe)
admin.site.register(Device)
admin.site.register(PublicAd,publicpadmin)
admin.site.register(RamDevice)
admin.site.register(StorgeDevice)
admin.site.register(TypeBreaks)
admin.site.register(Maintainaces)

# Register your models here.
