Nikita Horb Portfolio

To run the project you should run

1. `pip install -r requirements.txt`
2. specify .env file with

```
DATABASE_URL=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`