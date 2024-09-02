from django.contrib import admin
from .models import Workers

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name','location','age','work_category')


admin.site.register(Workers,WorkerAdmin)