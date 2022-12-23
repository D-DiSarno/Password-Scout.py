from actions import *
from Server import *

import pyfiglet


def login():
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

    # send credenziali a Esp-metodo getUser


def select_actions(connection):
    while True:
        print("\n\n##################################\n"
              "# Select an action:              #\n"
              "# 1. Login                       #\n"
              "# 2. Create new user             #\n"
              "# 3. Add credential              #\n"
              "# 4. Delete credential           #\n"
              "# 5. Show credential             #\n"
              "# 'quit' to Exit                 #\n"
              "##################################\n")
        print("\nInsert action: ")

        option = input()
        if option == '1':
            print("\n add_credential(json_credentials, connection)")
        elif option == '2':
            print("\n update_credential(json_credentials, connection)")
        elif option == '3':
            print("\n delete_credential(json_credentials, connection)")
        elif option == '4':
            print("\n view_credential(json_credentials, connection)")
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

    try:
        init_server()
    except:
        print("\n[ERROR] Something was wrong: connection refused.")
