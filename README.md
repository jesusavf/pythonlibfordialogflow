# python librery for dialogflow
Es una librería de python con flask que permite usar dialogflow por su interfaz
<h1>Guía de uso</h1>
Esta libreria se maneja por el index.py el cual es llamado con la libreria llamada py la cual se encarga de dar los mensajes deseados
<h1>Índice</h1>
<a href="#Instalar-flask">instalar flask</a>
<br>
<a style="margin-left:20px;" href="#Como-instalo-una-maquina-virtual">como instalar una maquina virtual</a>
<br>
<a href="#instalar-envios-request">instalar request</a>
<br>
<a href="#instalar-envios-jsonify">instalar jsonify</a>
<br>
<a href="#guía-de-uso-1">como usarlo</a>
<h1>instalaciones</h1>
<h2>Instalar flask</h1>
dentro de una maquina virtual intale este codigo
<b>pip install Flask</b><br>
<b>nota:</b> para verificar la instalacion se necesita el codigo <b>pip freeze</b>
<h3>Como instalo una maquina virtual</h2>
al tener python instalado en el archivo de lotes path se tiene un comando llamado <b>pip</b> el cual es el encargado de instalar paquetes<br>
como primero utilize este codigo en el directorio deseado.<b>python3 -m venv venv</b> o <b>python -m venv venv</b> o <b>py -3 -m venv venv</b> o <b>python2 -m virtualenv venv</b> si es la version dos de python.<br>
despues de eso acceda a la maquina virtual con este codigo <b>. venv/bin/activate</b> o <b>venv\Scripts\activate</b><br>
despues instalamos con <b>pip install Flask</b><br>
<b>nota:</b> para verificar la instalacion se necesita el codigo <b>pip freeze</b>
<h2>instalar envios request</h2>
Esta libreria sirve para recoger los datos deseados por metodos POST, GET ,HEADERS tanto como datos del servidor para instalarlo basta ponerlo en la maquina virtual este codigo <b> pip install request</b>
<h2>instalar envios jsonify</h2>
Esta libreria crea argumentos para poder tirar las variables de una manera comoda.<br>
para instalar basta con poner en la maquina virtual este codigo <b> pip install jsonify</b>
<h2>instalar para linux y mac</h2>
<b>nota: si este es subido ha heroku puede usarse en windows</b>
<h3>instalar gunicorn</h3>
 para proceder con la instalacion se puede con la instalacion basta con poner en la linea de comandos <b>pip install gunicorn</b>
 <h3>instalar waitress</h3>
 para proceder con la instalacion basta con la instalacion de waitress es tan simple como poner en la linea de comandos <b>pip install waitress</b><br>
 <b>nota: para poder usar el index para windows ocupas como primero configurar indexparawindows.py a app.run(host='0.0.0.0', port=3000) como el deseado como ejemplo:  app.run(host='127.0.0.1', port=3000) </b>
 <h2>sitios adaptados para esta libreria</h2>
<ul>
 <li>heroku</li>
 <li>docker</li>
</ul>
<h1>guía de uso</h1>
<h2>nota para windows</h2>
si esta usando windows home necesita subirlo a algun servidor o eliminar index.py para remplazarlo por indexparawindows.py y no correrlo por gunicorn si no por <b>python indexparawindows.py</b><br>
