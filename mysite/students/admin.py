from django.contrib import admin

# Register your models here.

from .models import Students, StudentInfo

admin.site.register(Students)
admin.site.register(StudentInfo)


