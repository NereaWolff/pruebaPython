# Prueba Técnica
### Ejercicio 1 : Python

### Indicaciones para ejecutar el proyecto

Éste fue realizado en Visual Studio Code y por medio del framework Django. Se recomienda seguir estos pasos para que la aplicación se ejecute correctamente

1. Una vez iniciado el proyecto, abrir una terminal (ctrl+ñ o Terminal/New Terminal en el menú superior de VS Code)
2. revisar el documento REQUIREMENTS.TXT incluido en los archivos del proyecto
3. en la terminal, ejecutar el siguiente comando " pip install -r requirements.txt " o en su defecto hacer la instalación directa de los complementos con " pip install django djangorestframework djangorestframework-simplejwt django-model-utils "
4. crear un superusuario con " python manage.py createsuperuser "
5. realizar las migraciones con " python manage.py makemigrations " y " python manage.py migrate "
6. el servidor se inicia con " python manage.py runserver ", hasta aquí debería ejecutarse sin menor inconveniente.


*En caso de iniciar el proyecto en SO basados en Linux, cambiar pip y python, por pip3 y python3 respectivamente.





Para fines prácticos se realizaron dos registros que deberían estar cargados en la base de datos de django una vez que se ingrese con el superusuario, con estos registros, se puede ejecutar la api desde sus urls definidos en el proyecto, e indicados a continuación:

- Para ingresar al administrador de Django:   127.0.0.1:8000/admin
- Método buscar por patente: 127.0.0.1:8000/buscarPatente/XXXXXXX/   *las X se reemplazan por la patente a buscar (valor alfanumérico de 4 letras y 4 números)
- Método buscar por id: 127.0.0.1:8000/buscarID/XXXXX/ *Las X se reemplazan por el id a buscar (debe ser numérico)

En caso de encontrar coincidencias, se mostrará la información por pantalla, de lo contrario, indicará que no se ha encontrado el registro que se busca.




### Desarrollado por Karen Lobos
#### 23/12/2021
