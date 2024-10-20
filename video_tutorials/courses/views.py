from django.shortcuts import render, get_object_or_404
from .models import Tutorial

def folder_list(request):
    # Fetch distinct folder paths
    folders = Tutorial.objects.values('folder_path').distinct()
    return render(request, 'courses/folder_list.html', {'folders': folders})

def tutorial_list(request, folder):
    # Fetch all tutorials in a specific folder
    tutorials = Tutorial.objects.filter(folder_path=folder)
    return render(request, 'courses/tutorial_list.html', {'tutorials': tutorials, 'folder': folder})

def tutorial_detail(request, pk):
    # Fetch a single tutorial by its primary key
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'courses/tutorial_detail.html', {'tutorial': tutorial})
