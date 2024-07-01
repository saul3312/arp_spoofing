para el archivo de ARP_spoofing.py se ejecuta en la maquina virtual de kali linux, yo lo hice con el adaptador puente, se ejecuta con el siguiente comando *sudo python ARP_spoofing.py*
En este programa se introduce primero la direccion router y luego la ip de la direccion de la maquina virtual de linux lite (o por lo menos asi lo hice yo)
Durante la ejecucion del codigo se mostraran varios WARNING pero aun asi durante ese bucle del programa se cambiara la direccion MAC y seran las mismas
Cuando se detenga el programa seguira durante un pequeño lapso de tiempo la direccion MAC igual, despues volvera a la anterior

Para el segundo programa que detecta algun cambio en la tabla ARP se tiene que crear un entorno virtual, y ejecute los siguientes comandos


*sudo apt install python3.12-venv*


*python3 -m venv myenv*


*source myenv/bin/activate*


Despues se ejecuta el programa *python detect_arp.py*
