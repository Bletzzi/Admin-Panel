#AdminPanel for Minecraft
import sys
import os
import subprocess
import time
import json
import createserver

def createServer():
    os.system("clear")
    print("Welcome to the Create Server Menu!")
    print("Please choose an Server EGG:")
    print("1. Spigot")
    print("2. Vanilla")
    print("3. BungeeCord")
    print("4. Bedrock")
    print("5. Back")
    choice = input("Please enter a number: ")
    if choice == "1":
        createserver.createSpigot()
    elif choice == "2":
        print("Coming soon!")
    elif choice == "3":
        print("Coming soon!")
    elif choice == "4":
        print("Coming soon!")
    elif choice == "5":
        main()

def main():
    print("Welcome to the AdminPanel for Minecraft!")
    print("Please choose an option:")
    print("1. Create a Minecraft Server")
    print("2. Manage a Minecraft Server")
    print("3. Exit")
    choice = input("Please enter a number: ")
    if choice == "1":
        createServer()
    elif choice == "2":
        print("Coming soon!")
    elif choice == "3":
        sys.exit()
    else:
        print("Please enter a valid number!")
        main()

main()
