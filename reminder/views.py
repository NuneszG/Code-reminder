from django.shortcuts import render, redirect
from .models import (
    Folder,
    Reminder
)

def Home(request):
    folders = Folder.objects.all()
    return render(request, 'home.html', {'folder': folders})


# Routes to folder
"""Acessar area que armazena todos os arquivos criados"""
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


"""Acessar uma pasta especifica por id"""
def GetFolder(request, id):
    folder = Folder.objects.get(id=id)
    file = Reminder.objects.all()
    return render(request, './folder/folder.html', {'folder': folder, 'files': file})


def EditFolder(request, id):
    folder = Folder.objects.get(id=id)
    return render(request, './folder/update.html', {'folder': folder})


def UpdateFolder(request, id):
    folder = Folder.objects.get(id=id)
    
    title = request.POST.get('title')
    category = request.POST.get('category')
    description = request.POST.get('description')

    folder.title = title
    folder.category = category
    folder.description = description
    folder.save()

    return redirect('folders')


def DeleteFolder(request, id):
    folder = Folder.objects.get(id=id)
    folder.delete()

    return redirect('home')


# Routes to files
def FormFile(request):
    return render(request, './files/form.html')

def CreateFile(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    file = Reminder.objects.create(
        title = title,
        content = content 
    )
    
    return redirect('folders')


def File(request, id):
    file = Reminder.objects.get(id=id)
    folder = Folder.objects.all()
    return render(request, './files/file.html', {'file': file, 'folder': folder})


def DeleteFile(request, id):
    file = Reminder.objects.get(id=id)
    file.delete()

    return redirect('folders')


def EditFile(request, id):
    file = Reminder.objects.get(id=id)
    return render(request, './files/update.html', {'file': file})

def UpdateFile(request, id):
    file = Reminder.objects.get(id=id)
    
    title = request.POST.get('title')
    content = request.POST.get('content')

    file.title = title
    file.content = content
    file.save()

    return redirect('folders')