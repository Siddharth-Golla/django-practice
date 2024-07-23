from django.contrib import admin
from .models import Project, ProjectImage, Tag

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    list_filter = ('tags',)
    search_fields = ('title', 'description', 'link')
    inlines = [ProjectImageInline]

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(Tag, TagAdmin)