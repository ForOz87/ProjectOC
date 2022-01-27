# ProjectOC

Ces scripts permettent l'installation et la configuration automatique
d'un serveur DHCP (isc-dhcp-server) et d'un serveur NTP (chrony).

Testé sur un système Ubuntu 20.04.3 LTS.

Utilisation

Utiliser la commande sudo pour ne pas avoir de problèmes de droits.

Copier les deux fichiers dhcp.py et ntp.py dans un repertoire de la machine.
Ouvrir le fichier dhcp.py et déclarer l'option générale et le sous réseau en
modifiant les parties suivantes :

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

Modifier la ligne suivante: fichier1.write("INTERFACES=\"enp0s3\"").
Remplacer enp0s3 par votre interface d'écoute.

NB: On peut déclarer plusieurs interfaces en ajoutant des espaces.
Exemple: "enp0s3 enp0s8".
Enregistrer le fichier.

Ouvrir le fichier ntp.py.
Modifier la ligne suivante par le réseau des clients : fichier.write("\nallow 192.168.1.0/24")
Enregistrer le fichier.

Autoriser l'execution des fichiers en tapant la ligne de commande suivante: sudo chmod +x dhcp.py ntp.py

Executer le fichier dhcp.py avec la commande suivante: sudo python3 dhcp.py
Le script fera automatiquement l'installation et la configureration de isc-dhcp-server.

Executer le fichier ntp.py avec la commande suivante: sudo python3 ntp.py
Le script va installer et configurer automatiquement chrony.
