from django.contrib import admin

# Register your models here.
from .models import Task, upload_account

class TaskAdmin(admin.ModelAdmin):
    list_display = ('created', 'active', 'completed', 'percentage_completed', 'errors' )



admin.site.register(Task, TaskAdmin)

