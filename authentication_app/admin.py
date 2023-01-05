from django.contrib import admin
from .models import *

class UI(admin.ModelAdmin):
    list_display=['fullname','username','city','state','money','id']
admin.site.register(UserInfo,UI)
