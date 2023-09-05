# FrontEnd

Se realizó una pequeña aplicación con Vue.js donde se consume una rest api para la administración de los empleados de una empresa. 

## Configuración del proyecto
### Instalación de dependencias
Se deben instalar las dependencias de node para el correcto funcionamiento
``` shell
cd front && npm install
```
### Configuración de variables
Se deben configurar las variables del archivo .env donde 

```
VUE_APP_API_URL= 'URL_del_servicio_FLASK'
BASE_URL= 'URL_del_FRONTEND'
```

Para tener el archivo .env y sus variables basta con 

```shell
cp .env.example .env
```

### Levantar el servidor

Solo resta correr el servido de vue con

```shell
npm run serve
```


