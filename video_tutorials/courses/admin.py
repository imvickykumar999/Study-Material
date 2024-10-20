from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_path')  # Display title, file path, and upload date
    search_fields = ('title', 'file_path')                # Add search functionality by title and file path

    # Make file_path field read-only since you're not uploading videos through admin
    readonly_fields = ('file_path',)

admin.site.register(Tutorial, TutorialAdmin)
