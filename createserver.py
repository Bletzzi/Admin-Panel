#AdminPanel for Minecraft
import sys
import os
import subprocess
import time
import json
import createserver

def checkServerStatus():
    print("Checking Server Status...")
    time.sleep(1)
    subprocess.call(["screen", "-S", "spigot", "-X", "stuff", "screen -S spigot -X stuff 'echo \"Server is running!\"\n'"])

def createSpigot():
    print("Creating Spigot Server...")
    time.sleep(1)
    #create a linux screen
    subprocess.call(["screen", "-dmS", "spigot"])
    #install spigot egg
    subprocess.call(["screen", "-S", "spigot", "-X", "stuff", "cd /home/minecraft/minecraft-server/ && wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar && java -jar BuildTools.jar --rev 1.12.2-R0.1-SNAPSHOT && rm BuildTools.jar && wget https://hub.spigotmc.org/jenkins/job/Spigot/lastSuccessfulBuild/artifact/spigot-1.12.2-R0.1-SNAPSHOT.jar && mv spigot-1.12.2-R0.1-SNAPSHOT.jar spigot.jar && screen -S spigot -X stuff 'java -Xmx1024M -Xms1024M -jar spigot.jar nogui'\n"])
    #start the server
    subprocess.call(["screen", "-S", "spigot", "-X", "stuff", "java -Xmx1024M -Xms1024M -jar spigot.jar nogui\n"])
    #wait for the server to start
    time.sleep(5)
    #check the server status
    checkServerStatus()
