# exchangeRate
Exchange rate, es un pequeño programa escrito en django, que registra el tipo de cambio que existe en una fecha, con este programa se puede obtener el precio de venta y compra que tiene un tipo de cambio, este dato se recolecta gracias al web service del banco de guatemala.

## Instalacion
Antes de seguir con la instalación, se adjunta un archivo requirement.txt que contiene los paquetes necesarios para su funcionamientos. Si desea instalarlos ejecute **pip3 install -r requirement.txt**

### Configuracion de la base de datos
Para este programa se hace uso de una base de datos sqlite, para usarlo es necesario ejecutar los siguientes comandos.
* python3 manage.py makemigrations (Busca los cambios si hubiera en los modelos y hace las migraciones)
* python3 manage.py migrate (Crea las tablas definidas antes en los modelos y posteriormente migradas)
* python3 manage.py runserver (Levanta la aplicación)
### Nota
* Si en dado caso, se ejecutara la aplicacion en una ip y puerto diferente, ir a exchange_rate>settings.py y cambiar la variable LOGIN_URL por la ruta raiz
