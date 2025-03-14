# Проект здоровье.

# Запуск проекта.

Установить докер.

### Настройка переменных окружения

Создайте файл .env в корне проекта, используя env.example в качестве шаблона:

   ```bash
    cp .env.example .env
   ```

или

   ```bash
   copy .env.example .env
   ```

Откройте файл .env и заполните необходимые переменные среды. Пример переменных и их описаний приведён в файле
.env.example.
Вставьте в него код

POSTGRES_USER=django_user
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_DB=foodgrgam
DB_NAME=foodgrgam_db_name

DB_HOST=db
DB_PORT=5432

SECRET_KEY='django-insecure-&g5#m@*bn1wi+*0wyqqwy9rofepf(re3@^gd3x+jrtbb#_%l+)'
DEBUG=True
ALLOWED_HOSTS=''

Файл .env используется для хранения переменных окружения, которые могут содержать конфиденциальные данные или настройки.

### Запуск и настройка проекта в докер контейнере.



Откройте консоль и введите команду в папке с файлом docker-compose.yml

   ```bash
  docker-compose up
   ```

Проведем миграции

   ```bash
   docker compose exec backend python manage.py migrate 
   ```

Сборка статики для корректной работы админки

   ```bash
   docker compose exec backend python manage.py collectstatic
   ```

   ```bash
   docker compose exec backend cp -r /app/backend_static/. /backend_static/static/ 
   ```

Загрузка ингредиентов в базу данных.

   ```bash
   docker-compose exec backend python manage.py import_ingredients
   ```

Загрузка тегов рецептов в базу данных.

   ```bash
   docker-compose exec backend python manage.py import_tags
   ```

Создание суперпользователя для входа в админку.

   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

Программа доступна по адресу.
http://localhost:8000/

# Просмотр документации.
### Чтобы открыть документацию зайдите в папку

foodgram-project-react\docs\redoc.html

И запустите html файл.

### Или нажмите на ссылку
http://localhost:63342/foodgram-health-project/docs/redoc.html?_ijt=r08pc87tjph83v65q2d7ot7ci2

### Пересборка образа

   ```bash
   docker compose up --build
   ```
 