# django-blog
Django simple blog

- `pipenv shell`

- `pipenv install`

> Make sure you have Pillow installed, if not just do `pip install Pillow`

> Create database in mysql and update db name in settings.py

``` json
DATABASES = {
    'default' : {
        ...
        'NAME': 'DB_NAME_HERE',
        ...
    }
}
```

- `python manage.py migrate`

- `python manage.py runserver`

Enjoy!