from django.urls import path
from .views import (
    Home,
    Folders,
    Form, 
    Create,
    GetFolder,
    DeleteFolder,
    CreateFile,
    FormFile,
    EditFolder,
    UpdateFolder,

    File, 
    DeleteFile,
    EditFile,
    UpdateFile,
)

urlpatterns = [
    path('', Home, name='home'),
    path('form-folder/', Form, name='form'),
    path('create-folder/', Create, name='create-folder'),
    path('folders/', Folders, name='folders'),
    path('get-folder/<int:id>/', GetFolder, name='folder'),
    path('edit-folder/<int:id>/', EditFolder, name='edit-folder'),
    path('delete-folder/<int:id>/', DeleteFolder, name='delete-folder'),
    path('update-folder/<int:id>/', UpdateFolder, name='update-folder'),

    path('form-file/', FormFile, name='form-file'),
    path('create-file/', CreateFile, name='create-file'),
    path('get-file/<int:id>/', File, name='file'),
    path('delete-file/<int:id>/', DeleteFile, name='delete-file'),
    path('edit-file/<int:id>/', EditFile, name='edit-file'),
    path('update-file/<int:id>/', UpdateFile, name='update-file'),


]