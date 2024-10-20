from django.shortcuts import render
from .models import Tutorial

def tutorial_list(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'courses/tutorial_list.html', {'tutorials': tutorials})
