#!/bin/bash

clear

echo "Installation script starting!"
echo "Running on user: $USER"
echo "Installing Python, Git, and python extensions!"
read -p "Are you sure? Y/N " -n 1 -r
echo    #
if [[ $REPLY =~ ^[Yy]$ ]]
then
        git clone https://github.com/KasperOnFire/ImpossibleTechnology.git
        apt update
        apt install -y git mysql-server python3-mysql.connector python3-pip python3-tk portaudio19-dev ffmpeg
        mysql_secure_installation
        pip3 install --upgrade pip
        pip3 install numpy
        pip install pydub
        pip install wavio
        pip install matplotlib
        pip install scipy
        pip install pyaudio
fi

echo "Please setup a database in MySQL and change it in Dejavu dejavu.cnf.SAMPLE"
