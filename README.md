# ProjectOC

Ces scripts permettent l'installation et la configuration d'un serveur DHCP et NTP.
A lancer avec sudo pour ne pas avoir de problèmes de droits.

Utilisation

Copier les deux fichiers dhcp.py et ntp.py, ouvrir le fichier dhcp.py et déclarer vos sous réseaux en modifiant la partie suivante:

fichier2.write("\n##### Option générale par défaut #####\n")
fichier2.write("\nserver-name \"dhcp.pz.oc\";")
fichier2.write("\noption domain-name-servers 8.8.8.8;")
fichier2.write("\ndefault-lease-time 7200;")
fichier2.write("\nmax-lease-time 7200;\n")

######## Déclaration de sous réseau #####################################
fichier2.write("\n#### Déclaration de sous réseaux ####\n")
fichier2.write("\n##### sous réseau 1 #####\n")
fichier2.write("\nsubnet 192.168.1.0 netmask 255.255.255.0 {")
fichier2.write("\nrange 192.168.1.1 192.168.1.253;")
fichier2.write("\noption routers 192.168.1.254;")
fichier2.write("\noption domain-name-servers 192.168.13.1;")
fichier2.write("\n}\n")

Modifier la ligne suivante en remplaçant enp0s3 par votre interface d'écoute:

fichier1.write("INTERFACES=\"enp0s3\"")

NB: On peut déclarer plusieurs interfaces d'écoutes en ajoutant des espaces.
Enregistrer le fichier.


Autoriser l'execution des fichiers en tapant la ligne de commande suivante: sudo chmod +x dhcp.py ntp.py

Executer les fichiers avec les commandes suivantes: sudo python3 dhcp.py
sudo python3 dhcp.py ntp.py
