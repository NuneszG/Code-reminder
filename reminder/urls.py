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
)

urlpatterns = [
    path('', Home, name='home'),
    path('form-folder/', Form, name='form'),
    path('create-folder/', Create, name='create'),
    path('folders/', Folders, name='folders'),
    path('get-folder/<int:id>/', GetFolder, name='folder'),
    path('edit-folder/<int:id>/', EditFolder, name='edit'),
    path('delete-folder/<int:id>/', DeleteFolder, name='delete-folder'),
    path('update-folder/<int:id>/', UpdateFolder, name='update'),

    path('form-file/', FormFile, name='form-file'),
    path('create-file/', CreateFile, name='create-file'),


]