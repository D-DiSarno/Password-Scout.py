from actions import *
from Server import *

import pyfiglet

logged = False
username = ""
password = ""
rfidAuthenticated = False

'''def login():
    while True:
        print('\n --- Insert username --- ')
        username = input()
        if username == "":
            print(" ERROR - Username cannot be null \n")
            continue
        print('\n --- Insert password --- ')
        password = input()
        if password == "":
            print(" ERROR - Passowrd cannot be null \n")
            continue


def signup():
    while True:
        print('\n --- Insert username --- ')
        username = input()
        if username == "":
            print(" ERROR - Username cannot be null \n")
            continue
        print('\n --- Insert password --- ')
        password = input()
        if password == "":
            print(" ERROR - Passowrd cannot be null \n")
            continue
    return'''


def select_actions(connection):
    while True:
        if logged:
            #QUI RFID
            print("--- Scan the RFID card ---")
            while rfidAuthenticated == False:
              #fino a quando è falsa non fa niente
              rfidAuthentication(connection)

            print("\n\n##################################\n"
                  "# Select an action:              #\n"
                  "# 1. Add credential              #\n"
                  "# 2. Delete credential           #\n"
                  "# 3. Show credential             #\n"
                  "# 'quit' to Exit                 #\n"
                  "##################################\n")
            print("\nInsert action: ")

            option = input()
            if option == '1':
                print("\n add_credential(service, password)")
            elif option == '2':
                print("\n delete_credential(service)")
            elif option == '3':
                print("\n view_credential(service)")
            elif option == 'quit':
                exit_connection(connection)
            else:
                while True:
                    print("Option not valid. Retry [Y/n]")
                    select = input()

                    if select.casefold() == 'y':
                        break
                    elif select.casefold() == 'n':
                        return
        else:
            print("\n\n##################################\n"
                  "# Select an action:              #\n"
                  "# 1. Login                       #\n"
                  "# 2. Register                    #\n"
                  "##################################\n")
            print("\nInsert action: ")

            option = input()
            if option == '1':
                print("\n login_user(username, password)")

            elif option == '2':
                print('\n--- Register user ---')

                while True:
                    print("Insert your username: ")
                    _username = input().strip()
                    print(f"Is '{_username}' correct? [Y/n]")
                    option = input()
                    if option.casefold() == 'y':
                        if _username == "":
                            print(" ERROR - The username cannot be null \n")
                            continue
                    elif option.casefold() == 'n':
                        continue
                    break

                while True:
                    print("Insert your password: ")
                    _password = input().strip()
                    print(f"Is '{_password}' correct? [Y/n]")
                    option = input()
                    if option.casefold() == 'y':
                        if _password == "":
                            print(" ERROR - The password cannot be null \n")
                            continue
                    elif option.casefold() == 'n':
                        continue
                    break

                if register_user(connection, _username, _password):
                    username = _username
                    password = _password
                    logged = True

            elif option == 'quit':
                exit_connection(connection)

            else:
                while True:
                    print("Option not valid. Retry [Y/n]")
                    select = input()

                    if select.casefold() == 'y':
                        break
                    elif select.casefold() == 'n':
                        return


if __name__ == '__main__':
    print(pyfiglet.figlet_format(" Password\n     Scout", font="slant"))
    init_server()
