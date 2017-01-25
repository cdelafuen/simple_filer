from django.contrib import admin

# Register your models here.
from filer.models import FileLog

admin.site.register(FileLog)
