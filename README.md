# Arctic Monkeys - Pagina Tributo
Sitio web tributo de Arctic Monkeys con Django.

Online: https://am-pagina-tributo.herokuapp.com/

## Cambiar Secret Key

Luego de instalar correr:

```python manage.py djecrety -d arcticMonkeys```

Con la secret key generada, la copiamos y agregamos en este comando

```heroku config:set SECRET_KEY="SECRET_KEY"```

Y lo ejecutamos en heroku.

### Requisitos

```asgiref==3.2.10
dj-database-url==0.5.0
Django==3.1
djecrety==1.0.13
gunicorn==20.0.4
pytz==2020.1
sqlparse==0.3.1
whitenoise==5.2.0```
