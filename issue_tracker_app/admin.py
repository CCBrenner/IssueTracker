from django.contrib import admin
# from django.db import models
# from django.forms import TextInput, Textarea
from .models import Project, Issue


class ProjectAdmin(admin.ModelAdmin):
    # Adds model columns to admin table display
    list_display = ['title', 'description', 'date_created', 'owner']

    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'20'})},
    #     models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    # }


class IssueAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'parent_project', 'date_created', 'last_updated', 'creator',
                    'worker', 'priority', 'difficulty']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)
