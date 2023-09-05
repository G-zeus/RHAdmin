# BackEnd

Api rest construida con Flask para la administracion de la informacion de empleados. Se implementó el patron repositorio para realizar las consultas a la base de datos. 
## Configuración del proyecto
### Instalar dependencias
Lo primero es instalar las dependencias de python que se encuentran en el archivo [requirements.txt](requirements.txt). Se recomienda usar un ambiente virtual con la version **3.10** de **Python**
``` shell
python3 -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
```
### Configuración de variables
Se deben configurar las variables del archivo .env donde

```
DEBUG=True
TESTING=True
SECRET_KEY='app secret key'
SQLALCHEMY_DATABASE_URI=' url de conexion con mySQL'
JWT_KEY= 'key para la creacion de JWT'
API_DOMAIN='dominio de la FLASk api'
APP_DOMAIN='dominio del frontend'

```

Para tener el archivo .env y sus variables basta con

```shell
cp .env.example .env
```

### Levantar el servidor

Solo resta correr el servido de Flask con el comando

```
flask --app app run --debug 
```

### Usuario de la App

Se necesita tener un usuario en la aplicación para poder acceder a los endpoints protejidos, por el momento solo es posible mediante POSTMAN o una petición curl

```shell
curl --location 'API_FLASK_URL/api/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"EMAIL_USER",
    "password":"CONTRASEÑA_USER"
}'
```
