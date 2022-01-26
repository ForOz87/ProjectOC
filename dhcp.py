#!/usr/bin/python

# Ce script permet l'installation et la configuration d'un serveur dhcp #
######## Il a été testé sur un système Ubuntu 20.04 LTE ################# 

import os
######## Installation du serveur dhcp ###################################
os.system("apt-get install -y isc-dhcp-server")

######## Emplacement des fichiers de configuration ######################
fichier1 = open("/etc/default/isc-dhcp-server","w")
fichier2 = open("/etc/dhcp/dhcpd.conf","w")

######## Editer le fremier fichier de configuration #####################
fichier1.write("INTERFACES=\"enp0s3\"")

######## Fermer le premier fichier de configuration #####################
fichier1.close()

######## Editer le deuxième fichier de configuration ####################
######## Option générale ################################################
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

######## Fermer le deuxième fichier de configuration ####################
fichier2.close()

######## Redémarrer le service dhcp ##################################### 
os.system("service isc-dhcp-server restart")