from django.contrib import admin
from projects.models import Project
from projects.models import DataSet

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Project infomation',               {'fields': ['name', 'description', 'dataset']}),
        ('Date information', {'fields': ['create_time'], 'classes': ['collapse']}),
    ]
admin.site.register(Project, ProjectAdmin)
admin.site.register(DataSet)