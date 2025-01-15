Manual del Programador
El código fuente está escrito en Python usando Flask y Authlib. El proyecto consta de los siguientes pasos principales:
1.	Instalación:
o	Instalar dependencias usando pip install Flask Authlib.
2.	Configurar la aplicación de GitHub:
o	Crear una aplicación en GitHub Developers y obtener el client_id y client_secret.
o	Asegurarse de que los parámetros de configuración en Flask coincidan con la configuración de GitHub.
3.	Archivo principal (app.py): El archivo principal es donde se gestionan las rutas de la aplicación, la autenticación, y la interacción con la API de GitHub.
Instrucciones para iniciar la aplicación:
•	Ejecutar flask run en el terminal.
•	Visitar la URL local, generalmente http://localhost:5000/.

Manual del Usuario
1.	Accede a la página web de la aplicación.
2.	Haz clic en el botón de Iniciar sesión con GitHub.
3.	Serás redirigido a GitHub para autorizar la aplicación.
4.	Una vez autorices la aplicación, serás redirigido de vuelta y verás un mensaje de bienvenida con tu nombre de usuario.
