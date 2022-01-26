#!/usr/bin/python

## Ce script permet l'installation et le parametrage du serveur ntp "chrony" #
####### Testé sur un système ubuntu version 20.04 lte ########################

import os
####### installation de chrony ###############################################
os.system("apt-get install -y chrony")

####### emplacement du fichier de configuration ##############################
fichier = open("/etc/chrony/chrony.conf","w")

####### edition du fichier ###################################################
fichier.write("\npool ntp.ubuntu.com iburst maxsources 4")
fichier.write("\npool 0.ubuntu.pool.ntp.org iburst maxsources 1")
fichier.write("\npool 1.ubuntu.pool.ntp.org iburst maxsources 1")
fichier.write("\npool 2.ubuntu.pool.ntp.org iburst maxsources 2")
fichier.write("\nkeyfile /etc/chrony/chrony.keys")
fichier.write("\ndriftfile /var/lib/chrony/chrony.drift")
fichier.write("\nlogdir /var/log/chrony")
fichier.write("\nmaxupdateskew 100.0")
fichier.write("\nrtcsync")
fichier.write("\nmakestep 1 3")
fichier.write("\nallow 192.168.1.0/24")

####### quitter le fichier ###################################################
fichier.close()

####### lancer chrony au demarrage systeme ###################################
os.system("systemctl enable chrony")

####### desactiver le service NTP par défaut #################################
os.system("timedatectl set-ntp false")

####### demarrer le service ##################################################
os.system("systemctl start chrony")
