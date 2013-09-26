from django.contrib import admin
from cgadmin.models import User,Post,Project,Team,File,Announcment,Enterprise

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username','email','headimg')
    search_fields = ('username','email')


class FileAdmin(admin.ModelAdmin):
    list_display = ('file_disc','project','fcreate_date','create_user')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name','parent','disc')
    filter_horizontal = ('member',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_disc','pcreate_date')
    filter_horizontal = ('project_admin',)

class AnnounAdmin(admin.ModelAdmin):
    list_display = ('announ_title','announ_user','announ_date')
    filter_horizontal = ('announ_obj','announ_enterprise')

admin.site.register(User,UsersAdmin)
admin.site.register(Post)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(File,FileAdmin)
admin.site.register(Announcment,AnnounAdmin)
admin.site.register(Enterprise)