from django.contrib import admin
from .models import Info
# # Register your models here.

admin.site.register(Info)


admin.site.site_header = "CODEd"
admin.site.index_title= "Welcome to CODEd"
admin.site.site_title= "World's best BlogApp"

