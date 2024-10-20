import os
from courses.models import Tutorial

def scan_videos_and_add_to_db():
    base_path = 'media/videos/'  # Adjust this if your path is different
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(('.mp4', '.mov', '.avi', '.mkv')):  # Add other formats if needed
                relative_file_path = os.path.relpath(os.path.join(root, file), base_path)
                folder_path = os.path.relpath(root, base_path)  # Store relative folder path
                title = os.path.splitext(file)[0]  # Use filename as the title
                
                # Create or update the Tutorial entry
                Tutorial.objects.get_or_create(
                    title=title,
                    folder_path=folder_path,
                    file_path=relative_file_path
                )

# Run this function in Django shell to populate the database
scan_videos_and_add_to_db()
