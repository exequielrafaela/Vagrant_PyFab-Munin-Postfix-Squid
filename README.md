# Vagrant_PyFab-Munin-Postfix-Squid
Vagrant + Python Fabrico to provision: Munin Monitoring Service, Postfix Internet Email Service, Squid HTTP Proxy, Apache2 Web Server, IPTables FW, NFS (Network File System) and Logrotate

Just clone and then "vagrant up"

Enjoy!

Parcial II

El trabajo práctico II consiste en las siguientes tareas:

1.- Instalación de servicio munin.

1.1.- Monitorear localhost.

1.2.- Asegurar que se encuentren los siguientes servicios monitoreados

1.2.1.- munin, apache*, postfix*, firewall*, nfs*, squid*

2.- Configuración de firewall

2.1- Configurar el firewall para que el servidor pueda realizar cualquier conexión saliente, pero solo pueda recibir conexiones para los servicios configurados.
Solo se deben aceptar conexiones de la red a la cual pertenece el servidor.

3.- Configuración de servidor de correo

3.1.- Implementar un servidor de mail, utilizar el relayhost = 'tortuga.unc.edu.ar' y enviar un correo a ermirizio@gmail.com

3.2.- Crear un dominio de mail, con un correo electrónico asociado:

3.2.1.- Dominio 'apellido del alumno'

3.2.2.- nombre-del-alumno@apellido-del-alumno

4.- Configuración de servidor proxy HTTP

4.1.- El acceso al servicio de proxy será de manera explícita y será con autenticación.

4.1.1.- Usuario: nombre. Password: apellido

4.2.- Solo permitirá navegación a equipos se se encuentren en la misma red.

4.3.- Implementar y aplicar una regla que evite acceder a los siguientes sitios:

www.infobae.com/radio10/radio10-en-vivo.php

cadena3.com.ar/multimedia.asp

www.cadena3.com.ar/multimedia.asp

cadena3.com.ar/audios.asp

cadena3.com/multimedia.asp

cadena3.com/audios.asp

lv3.com.ar/multimedia.asp

lv3.com.ar/audios.asp

www.la100.com.ar/aspx/reproductor/reproductor.html

www.radiomitre.com.ar/popup_audio.asp

www.am970.com.ar/windowsmedia/lv2_envivo.htm

www.continental.com.ar/player.aspx

www.amdelplata.com/reproductor/reproductor2.php

www.amradioamerica.com/live.html

www.ambelgrano.com/site/programacion/radio.html

www.rivadavia.com.ar/streaming16/

mega.10musica.com/Radio

los40principales.com.ar/player/Radio/40Principales/index.html

www.fmrockandpop.com/index.php?option=com_content&view=article&id=114&Itemid=92

www.fmaspen.com/reproductor.htm

5.- Configuración de servidor NFS

5.1.- Compartir el directorio /srv/nfs a la red a la cual pertenece el servidor. Debe tener permiso de lectura y escritura. Tratar al usuario 'root' remoto como usuario 'nobody'

6.- Configuración LVM (NO REALIZAR)

6.1.- En virtualbox crear un logical volume de 512MB llamado 'nombre-del-alumno' que pertenezca al volume group 'apellido-del-alumno'.

6.2.- Configurar este LV para que se monte automáticamente cuando bootee el servidor en /srv/nfs

7.- Configuración Apache

7.1.- Configurar apache para que solo funcione en HTTPS puerto 443.

8.- Configuración de logrotate

8.1.- Configurar la rotación de logs para que no superen los 30 días de almacenamiento. Todo log se debe rotar una vez por día. El resto de las opciones dejar por defecto. Esto aplica a los logs de los siguientes servicios:
- Apache

- Squid

- Postfix

9.- Informe

9.1.- Subir el informe de todo lo realizado a la plataforma virtual en formato PDF respetando la siguiente nomenclatura: csl-Apellido-Nombre-TP2.pdf

9.2. Usar el template del Trabajo Práctico 1.
