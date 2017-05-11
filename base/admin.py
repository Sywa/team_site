from django.contrib import admin
from .models import Team, Projects, Contact

class TeamAdmin(admin.ModelAdmin):
    model = Team
admin.site.register(Team, TeamAdmin)

class ProjectsAdmin(admin.ModelAdmin):
    model = Projects
admin.site.register(Projects, ProjectsAdmin)

class ContactAdmin(admin.ModelAdmin):
    model = Contact
admin.site.register(Contact, ContactAdmin)
