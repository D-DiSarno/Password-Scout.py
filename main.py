import time

from actions import *
from Server import *

import pyfiglet


def select_actions(connection):
    logged = False
    username = ""
    password = ""
    tag = ""

    while True:
        time.sleep(3.5)
        if logged:
            print("\n\nO--------------------------------O\n"
                  "| Select an action:              |\n"
                  "| 1. Add credentials             |\n"
                  "| 2. Delete credentials          |\n"
                  "| 3. Show credentials            |\n"
                  "| 4. Logout                      |\n"
                  "| 'quit' to Exit                 |\n"
                  "O--------------------------------O\n")
            print("Insert action: ", end="")
            option = input()

            if option == '1':
                add_credential(connection, username, password, tag)
            elif option == '2':
                delete_credential(connection, username, password, tag)
            elif option == '3':
                view_credential(connection, username, password, tag)
            elif option == '4':
                print(f"See you soon, {username}!")
                logged = False
                username = ""
                password = ""
                tag = ""
            elif option == 'quit':
                exit_connection(connection)
            else:
                while True:
                    print("Option not valid. Retry? [Y/n] ", end="")
                    select = input()

                    if select.casefold() == 'y':
                        break
                    elif select.casefold() == 'n':
                        exit_connection(connection)
        else:
            print("\n\nO--------------------------------O\n"
                  "| Select an action:              |\n"
                  "| 1. Login                       |\n"
                  "| 2. Register                    |\n"
                  "| 'quit' to Exit                 |\n"
                  "O--------------------------------O\n")
            print("Insert action: ", end="")
            option = input()

            if option == '1':
                print("\n --- Login ---")
                while True:
                    print("Insert your username: ", end="")
                    _username = input().strip()
                    if _username == "":
                        print("ERROR - The username cannot be null")
                        continue
                    else:
                        break

                while True:
                    print("Insert your password: ", end="")
                    _password = input().strip()
                    if _password == "":
                        print("ERROR - The password cannot be null")
                        continue
                    else:
                        break

                _res = login_user(connection, _username, _password)
                if _res != "":
                    username = _username
                    password = _password
                    tag = _res
                    logged = True
            elif option == '2':
                print('\n--- Register user ---')

                while True:
                    print("Insert your username: ", end="")
                    _username = input().strip()
                    if _username == "":
                        print("ERROR - The username cannot be null \n")
                        continue
                    print(f"Is '{_username}' correct? [Y/n] ", end="")
                    option = input()
                    if option.casefold() == 'y':
                        break
                    elif option.casefold() == 'n':
                        continue

                while True:
                    print("Insert your password: ", end="")
                    _password = input().strip()
                    if _password == "":
                        print("ERROR - The password cannot be null \n")
                        continue
                    print(f"Is '{_password}' correct? [Y/n] ", end="")
                    option = input()
                    if option.casefold() == 'y':
                        break
                    elif option.casefold() == 'n':
                        continue

                _res = register_user(connection, _username, _password)
                if _res != "":
                    username = _username
                    password = _password
                    tag = _res
                    logged = True
            elif option == 'quit':
                exit_connection(connection)
            else:
                while True:
                    print("Option not valid. Retry? [Y/n] ", end="")
                    select = input()

                    if select.casefold() == 'y':
                        break
                    elif select.casefold() == 'n':
                        exit_connection(connection)


if __name__ == '__main__':
    print(pyfiglet.figlet_format(" Password\n     Scout", font="slant"))
    init_server()
