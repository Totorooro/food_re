# FlavorFeed Project  

---
## Документация по запуску  


---
### 1. Склонировать репозиторий

---
```
git clone <ссылка на репо>
cd <папка проекта>
```

### 2. Создать виртуальное окружение

---
```
python -m venv .venv
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate       # Windows
```

### 3. Настройка .env

--- 
Создать файл .env в корне проекта с следующим содержимым:
```
SECRET_KEY=your_secret_key
DB_NAME=flavorfeed_db
DB_USER=your_username
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 4. Запуск докера 

---
```
docker-compose up --build
```

### 5. Сделать миграции и админа

---
Для этого нужно октрыть еще одну консоль, перейти в папку проекта и запустить:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser       
```

### 6. Наполнить тестовыми данными

---
```
docker-compose exec web python manage.py loaddata recipes_recipes.json recipes_cat.json  
```