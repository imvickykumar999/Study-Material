from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'folder_path', 'file_path')  # Display title, folder path, and file path
    search_fields = ('title', 'folder_path', 'file_path')  # Search by title, folder path, and file path
    list_filter = ('folder_path',)  # Filter by folder path to easily find tutorials by folder
    ordering = ('folder_path', 'title')  # Order by folder path and title

    readonly_fields = ('file_path', 'folder_path')  # Make both file and folder paths read-only

admin.site.register(Tutorial, TutorialAdmin)
