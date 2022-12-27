from actions import *
from Server import *

import pyfiglet


def select_actions(connection):
    logged = False
    username = ""
    password = ""
    tag = ""

    while True:
        if logged:
            print("\n\n##################################\n"
                  "# Select an action:              #\n"
                  "# 1. Add credentials             #\n"
                  "# 2. Delete credentials          #\n"
                  "# 3. Show credentials            #\n"
                  "# 4. Logout                      #\n"
                  "# 'quit' to Exit                 #\n"
                  "##################################\n")
            print("\nInsert action: ")
            option = input()

            if option == '1':
                add_credential(connection, username, password, tag)
            elif option == '2':
                delete_credential(connection, username, password, tag)
            elif option == '3':
                view_credential(connection, username, password, tag)
            elif option == '4':
                logged = False
                username = ""
                password = ""
                tag = ""
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
                  "# 'quit' to Exit                 #\n"
                  "##################################\n")
            print("\nInsert action: ")
            option = input()

            if option == '1':
                print("\n --- Login ---")
                while True:
                    print("Insert your username: ")
                    _username = input().strip()
                    if _username == "":
                        print(" ERROR - The username cannot be null \n")
                        continue
                    else:
                        break

                while True:
                    print("Insert your password: ")
                    _password = input().strip()
                    if _password == "":
                        print(" ERROR - The password cannot be null \n")
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
                    print("Option not valid. Retry [Y/n]")
                    select = input()

                    if select.casefold() == 'y':
                        break
                    elif select.casefold() == 'n':
                        return


if __name__ == '__main__':
    print(pyfiglet.figlet_format(" Password\n     Scout", font="slant"))
    init_server()
