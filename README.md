# Arctic Monkeys - Pagina Tributo
Sitio web tributo de Arctic Monkeys con Django.

Online: https://am-pagina-tributo.herokuapp.com/

## Cambiar Secret Key

Luego de instalar correr:

&nbsp; ```python manage.py djecrety```

Nos va a generar una nueva SECRET_KEY, procedemos a copiarla.

El valor de SECRET_KEY debe guardarse como variable de entorno.

* Windows10

&nbsp; ``` setx SECRET_KEY "VALOR OBTENIDO DEL COMANDO DJECRETY" ```

* Linux Debian/Ubuntu

&nbsp; ``` sudo nano /etc/environment ```

&nbsp; Al final del archivo agregamos:

``` SECRET_KEY = "VALOR OBTENIDO DEL COMANDO DJECRETY" ```

* Heroku CLI

&nbsp; ``` heroku config:set SECRET_KEY="VALOR OBTENIDO DEL COMANDO DJECRETY" ```

Con esto ya estammos listos para correr nuestra instalacion.

El usuario administrador es 'monkeyadm', sus credenciales se pueden reiniciar desde la consola.

### Requisitos

```asgiref==3.2.10
dj-database-url==0.5.0
Django==3.1
djecrety==1.0.13
gunicorn==20.0.4
pytz==2020.1
sqlparse==0.3.1
whitenoise==5.2.0```
