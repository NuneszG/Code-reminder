# Code Reminder

O Code Reminder é um website de organização para o usuário.
No qual o usuário pode criar pastas com determinado titulo e categoria, e dentro delas podendo criar arquivos
para deixar salvo determinado assunto que elas queiram guardar e reve-los depois.

### Features
- create new folders to organize your data into files
- create a new file and save your data into it 
- update both your folder and files 
- delete any folder or files you want 

### Technologies used
- Python
- Django 
- PostgreSQL 
- Bootstrap 

<div style="display: grid; grid-template-columns: repeat(2, 400px); gap: 10px;">
    <img src="/assets/application/Captura de ecrã 2024-11-15 170507.png" style="width: 376px">
    <img src="/assets/application/Captura de ecrã 2024-11-15 182938.png" style="width: 447px">
    <img src="/assets/application/Captura de ecrã 2024-11-15 170528.png" style="width: 427px">
    <img src="/assets/application/Captura de ecrã 2024-11-15 170845.png" style="width: 437px">
</div

### Clone repository
```
https://github.com/NuneszG/Code-reminder.git
```

### Docker 
```
create database image

docker-compose up database --build
```
```
create application image

docker-compose up reminder --build
```

### Run container
```
docker-compose up
```

### Access application container in the browser
```
http://localhost:8000
```

### Virtual space 
```
Linux or MacOS
source venv/bin/activate

Windows
./venv/Scripts/activate
```

### Install 
```
poetry install
```

### Run application  
```
With poetry
task server

Without poetry
python manage.py runserver
```
