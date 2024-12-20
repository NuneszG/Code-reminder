# Code Reminder

O Code Reminder é um website de organização para o usuário.
No qual o usuário pode criar pastas com determinado titulo e categoria, e dentro delas podendo criar arquivos
para deixar salvo determinado assunto que eles queiram guardar e reve-los depois.

### Features
- crie novas pastas para organizar seus dados nelas 
- crie um novo arquivo e salve seus dados  
- atualize tanto suas pastas quanto seus arquivos 
- delete qualquer pasta ou arquivo que desejar

### Technologies used
- Python
- Django 
- Docker
- PostgreSQL 
- Bootstrap 

<div style="display: grid; grid-template-columns: repeat(2, 400px); gap: 10px;">
  <img src="/assets/application/Captura de ecrã 2024-11-15 185342.png" style="width: 400px">
  <img src="/assets/application/Captura de ecrã 2024-11-15 185424.png" style="width: 400px">
  <img src="/assets/application/Captura de ecrã 2024-11-15 185440.png" style="width: 400px">
  <img src="/assets/application/Captura de ecrã 2024-11-15 185940.png" style="width: 400px">
</div>

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
