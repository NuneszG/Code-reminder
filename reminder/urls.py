from django.urls import path
from .views import (
    Home,
    Folders,
    Form, 
    Create,
)

urlpatterns = [
    path('', Home, name='home'),
    path('form-folder/', Form, name='form'),
    path('create-folder/', Create, name='create'),
    path('folders/', Folders, name='folders'),

]