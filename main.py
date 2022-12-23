from actions import *
from Server import *

import pyfiglet

logged = False
username = ""
password = ""


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
                register_user(connection)
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
