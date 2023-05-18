from django.contrib import admin
from .models import issue_type, issue, issue_file, issue_responders, issue_comment, issue_comment_file, task_category, task_file, task_responders, task_comment, task_comment_file, task_cetegory_theme, task_services

# Register your models here.
admin.site.register(issue_type)
admin.site.register(issue)
admin.site.register(issue_file)
admin.site.register(issue_responders)
admin.site.register(issue_comment)
admin.site.register(issue_comment_file)
admin.site.register(task_category)

class task_category_themeAdmin(admin.ModelAdmin):
	list_display = ('name', 'short_description')

admin.site.register(task_cetegory_theme, task_category_themeAdmin)



admin.site.register(task_services)
admin.site.register(task_file)
admin.site.register(task_responders)
admin.site.register(task_comment)
admin.site.register(task_comment_file)