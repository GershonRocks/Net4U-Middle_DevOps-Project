#!/usr/bin/env python3

import os

def menu():
    print('''
        1. Pull image (mynginx:ubuntu_22.04)
        2. Run X mynginx
        3. Remove Image/Container
        4. Run web app at specific port
        ''')
    choice = int(input("Enter your choice:"))

    if choice == 1:
        os.system('docker pull gtdreams/mynginx:ubuntu_22.04')
    elif choice == 2:
        number_of_container = int(input("Enter number of container: "))
        container_name = input("Enter container name: ")
        for index in range(1, number_of_container + 1):
            os.system(f"docker run -d --name {container_name}_{index} mynginx:ubuntu_22.04")
    elif choice == 3:
        type_of_command = input("Choose: Image / Container")
        if type_of_command.lower() == "image":
            image_name = input("Enter image name for removal: ")
            os.system(f"docker rmi -f {image_name}")
        elif type_of_command.lower() == "container":
            container_name = input("Enter container name for removal: ")
            os.system(f"docker rm -f {container_name}")
    elif choice == 4:
        number_of_container = int(input("Enter number of container: "))
        container_name = input("Enter container name: ")
        port_number = input("Enter ports pair to open <host>:<container>")
        for index in range(1, number_of_container + 1):
            os.system(f"docker run -d -p {port_number} --name {container_name}_{index} mynginx:ubuntu_22.04")
        
        
while True:
    menu()
    exit_menu = input("Do you want to continue running? yes/no")
    if exit_menu.lower() == "yes":
        continue
    else:
        print("Bye...")
        break
    