from django.contrib import admin
#
from .models import Course, Enrollment, Announcement, Comment, Lesson, Material
# models
#
class CourseAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'shortcut', 'created_on', 'updated_on']
    search_fields = ['name', 'shortcut']
    prepopulated_fields = {'shortcut': ('name',)}
#
class MaterialInLineAdmin(admin.TabularInline):
    
    model = Material
#
class LessonAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = [ 'name', 'description']
    list_filer = ['created_on']
    inlines = [ MaterialInLineAdmin]
#   
admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)