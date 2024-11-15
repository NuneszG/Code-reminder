from django.shortcuts import render
from .models import Folder

def Home(request):
    folders = Folder.objects.all()
    return render(request, 'home.html', {'folder': folders})


def Folders(request):
    folders = Folder.objects.all()
    return render(request, './folder/folders.html', {'folders': folders})


def Form(request):
    return render(request, './folder/form.html')

def Create(request):
    title = request.POST.get('title')
    category = request.POST.get('category')
    descripion = request.POST.get('description')

    folder = Folder.objects.create(
        title = title,
        category = category,
        description = descripion
    )
    return render(request, 'home.html', {'folder': folder})