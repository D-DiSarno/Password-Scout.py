import sys

import pandas as pd
import copy


'''
def add_credential(json_credentials, connection):
    if len(json_credentials) >= 100:
        print(" ERROR - No storage space avaible on ESP32 \n")
        return

    print('\n --- Insert new credentials --- ')

    while True:
        print('Please insert Application Name: ')
        name = input().strip()
        # print(f"Is '{name}' correct? [Y/n]")

        option = input()
        if option.casefold() == 'y':
            if name == "":
                print(" ERROR - The name cannot be null \n")
                continue

            flag = False
            for entry_name in json_credentials:
                if entry_name['name'] == name:
                    print(" ERROR - Name already stored in memory \n")
                    flag = True
                    break

            if not flag:
                while True:
                    print('\nPlease insert Username: ')
                    username = input().strip()
                    print(f"Is '{username}' correct? [Y/n]")

                    option = input()
                    if option.casefold() == 'y':
                        if username == "":
                            print(" ERROR - The username cannot be null \n")
                            continue

                        while True:
                            print('\nPlease insert Password: ')
                            password = input().strip()
                            print(f"Is '{password}' correct? [Y/n]")

                            option = input()
                            if option.casefold() == 'y':
                                if password == "":
                                    print(" ERROR - The password cannot be null \n")
                                    continue

                                entry_enc = {'name': name, 'username': '**************', 'password': '**************'}

                                json_credentials.append(entry_enc)
                                connection.sendall(b'1-' + name.encode('utf-8') +
                                                   b'-' + username.encode('utf-8') +
                                                   b'-' + password.encode('utf-8'))
                                return

                            elif option.casefold() == 'n':
                                continue

                            else:
                                if not option_invalid():
                                    return

                    elif option.casefold() == 'n':
                        continue

                    else:
                        if not option_invalid():
                            return

        elif option.casefold() == 'n':
            continue

        else:
            if not option_invalid():
                return


def update_credential(json_credentials, connection):
    print('\n--- Update credentials ---')

    while True:
        print('Select the name that needs to be update: ')
        old_name = input().strip()
        print(f"Is '{old_name}' correct? [Y/n]")

        option = input()
        if option.casefold() == 'y':
            for entry_name in json_credentials:
                if entry_name['name'] == old_name:
                    while True:
                        print('\nDo you want update name? [Y/n]')
                        option = input()

                        if option.casefold() == 'y':
                            while True:
                                print('Please insert name: ')
                                new_name = input().strip()
                                print(f"Is '{new_name}' correct? [Y/n]")

                                option = input()
                                if option.casefold() == 'y':
                                    if new_name == "":
                                        print(" ERROR - The name cannot be null \n")
                                        continue

                                    while True:
                                        print('\nDo you want update username? [Y/n]')
                                        option = input()

                                        if option.casefold() == 'y':
                                            while True:
                                                print('Please insert username: ')
                                                new_username = input().strip()
                                                print(f"Is '{new_username}' correct? [Y/n]")

                                                option = input()
                                                if option.casefold() == 'y':
                                                    if new_username == "":
                                                        print(" ERROR -  The username cannot be null \n")
                                                        continue

                                                    while True:
                                                        print('\nDo you want update password? [Y/n]')
                                                        option = input()

                                                        if option.casefold() == 'y':
                                                            while True:
                                                                print('Please insert password: ')
                                                                new_password = input().strip()
                                                                print(f"Is '{new_password}' correct? [Y/n]")

                                                                option = input()
                                                                if option.casefold() == 'y':
                                                                    if new_password == "":
                                                                        print(" ERROR - The password cannot be null \n")
                                                                        continue

                                                                    entry_name['name'] = new_name
                                                                    entry_name['username'] = new_username
                                                                    entry_name['password'] = new_password
                                                                    connection.sendall(b'2-' +
                                                                                       old_name.encode('utf-8') +
                                                                                       b'-' +
                                                                                       new_name.encode('utf-8') +
                                                                                       b'-' +
                                                                                       new_username.encode('utf-8') +
                                                                                       b'-' +
                                                                                       new_password.encode('utf-8'))
                                                                    return
                                                                elif option.casefold() == 'n':
                                                                    continue
                                                                else:
                                                                    if not option_invalid():
                                                                        return
                                                        elif option.casefold() == 'n':
                                                            entry_name['name'] = new_name
                                                            entry_name['username'] = new_username
                                                            connection.sendall(b'2-' + old_name.encode('utf-8') +
                                                                               b'-' + new_name.encode('utf-8') +
                                                                               b'-' + new_username.encode('utf-8') +
                                                                               b'-NULL')
                                                            return
                                                        else:
                                                            if not option_invalid():
                                                                return
                                                elif option.casefold() == 'n':
                                                    continue
                                                else:
                                                    if not option_invalid():
                                                        return
                                        elif option.casefold() == 'n':
                                            while True:
                                                print('\nDo you want update password? [Y/n]')
                                                option = input()

                                                if option.casefold() == 'y':
                                                    while True:
                                                        print('Please insert password: ')
                                                        new_password = input().strip()
                                                        print(f"Is '{new_password}' correct? [Y/n]")

                                                        option = input()
                                                        if option.casefold() == 'y':
                                                            if new_password == "":
                                                                print(" ERROR - The password cannot be null \n")
                                                                continue

                                                            entry_name['name'] = new_name
                                                            entry_name['password'] = new_password
                                                            connection.sendall(b'2-' + old_name.encode('utf-8') +
                                                                               b'-' + new_name.encode('utf-8') +
                                                                               b'-NULL-' + new_password.encode('utf-8'))
                                                            return
                                                        elif option.casefold() == 'n':
                                                            continue
                                                        else:
                                                            if not option_invalid():
                                                                return
                                                elif option.casefold() == 'n':
                                                    entry_name['name'] = new_name
                                                    connection.sendall(b'2-' + old_name.encode('utf-8') +
                                                                       b'-' + new_name.encode('utf-8') +
                                                                       b'-NULL-NULL')
                                                    return
                                                else:
                                                    if not option_invalid():
                                                        return
                                        else:
                                            if not option_invalid():
                                                return
                                elif option.casefold() == 'n':
                                    continue
                                else:
                                    if not option_invalid():
                                        return
                        elif option.casefold() == 'n':
                            print('\nDo you want update username? [Y/n]')
                            option = input()

                            if option.casefold() == 'y':
                                while True:
                                    print('Please insert username: ')
                                    new_username = input().strip()
                                    print(f"Is '{new_username}' correct? [Y/n]")

                                    option = input()
                                    if option.casefold() == 'y':
                                        if new_username == "":
                                            print(" ERROR - The username cannot be null \n")
                                            continue

                                        print('\nDo you want update password? [Y/n]')
                                        option = input()

                                        if option.casefold() == 'y':
                                            print('Please insert password: ')
                                            new_password = input().strip()
                                            print(f"Is '{new_password}' correct? [Y/n]")

                                            if option.casefold() == 'y':
                                                if new_password == "":
                                                    print(" ERROR - The password cannot be null\n")
                                                    continue

                                                entry_name['username'] = new_username
                                                entry_name['password'] = new_password
                                                connection.sendall(b'2-' + old_name.encode('utf-8') +
                                                                   b'-NULL-' + new_username.encode('utf-8') +
                                                                   b'-' + new_password.encode('utf-8'))
                                                return
                                            elif option.casefold() == 'n':
                                                continue
                                            else:
                                                if not option_invalid():
                                                    return
                                        elif option.casefold() == 'n':
                                            entry_name['username'] = new_username
                                            connection.sendall(b'2-' + old_name.encode('utf-8') +
                                                               b'-NULL-' + new_username.encode('utf-8') + b'-NULL')
                                            return
                                        else:
                                            if not option_invalid():
                                                return
                                    elif option.casefold() == 'n':
                                        continue
                                    else:
                                        if not option_invalid():
                                            return
                            elif option.casefold() == 'n':
                                print('\nDo you want update password? [Y/n]')
                                option = input()

                                if option.casefold() == 'y':
                                    print('Please insert password: ')
                                    new_password = input().strip()
                                    print(f"Is '{new_password}' correct? [Y/n]")

                                    if option.casefold() == 'y':
                                        if new_password == "":
                                            print(" ERROR - The password cannot be null \n")
                                            continue

                                        entry_name['password'] = new_password
                                        connection.sendall(b'2-' + old_name.encode('utf-8') +
                                                           b'-NULL-NULL-' + new_password.encode('utf-8'))
                                        return
                                    elif option.casefold() == 'n':
                                        continue
                                    else:
                                        if not option_invalid():
                                            return
                                elif option.casefold() == 'n':
                                    return
                                else:
                                    if not option_invalid():
                                        return
                            else:
                                if not option_invalid():
                                    return
                        else:
                            if not option_invalid():
                                return

            print(" ERROR - Name not in memory \n")
            print("Do you want to try again? [Y/n]")
            option = input()

            if option.casefold() == 'y':
                continue
            elif option.casefold() == 'n':
                return
            else:
                if not option_invalid():
                    return
        elif option.casefold() == 'n':
            continue
        else:
            if not option_invalid():
                return


def delete_credential(json_credentials, connection):
    print('\n--- Delete credentials ---')

    if len(json_credentials) <= 0:
        print(' ERROR -  Credentials list is empty! \n')
        return

    while True:
        print("Select the credential's name that do you want delete: ")
        name = input().strip()
        print(f"Is '{name}' correct? [Y/n]")

        option = input()
        if option.casefold() == 'y':
            for i in range(len(json_credentials)):
                if json_credentials[i]['name'] == name:
                    del json_credentials[i]
                    connection.sendall(b'3-' + name.encode('utf-8'))
                    return

            print(" ERROR -  Name not in memory \n")
            print("Do you want to try again? [Y/n]")

            option = input()
            if option.casefold() == 'y':
                continue
            elif option.casefold() == 'n':
                return
            else:
                if not option_invalid():
                    return
        elif option.casefold() == 'n':
            continue
        else:
            if not option_invalid():
                return


def decrypt_credentials(json_credentials, key):
    json_credentials_tmp = copy.deepcopy(json_credentials)
    c = "X"  # cipher.AES.new(key, cipher.MODE_ECB, b"sssssssss")
    print(key)

    for entry in json_credentials_tmp:
        entry['username'] = c.decrypt(entry['username'].encode()).decode('utf-8'),
        entry['password'] = c.decrypt(entry['password'].encode()).decode('utf-8'),

    print(pd.DataFrame(data=json_credentials_tmp))'''


def register_user(connection):
    print('\n--- Register user ---')

    while True:
        print("Insert your username: ")
        username = input().strip()
        print(f"Is '{username}' correct? [Y/n]")
        option = input()
        if option.casefold() == 'y':
            if username == "":
                print(" ERROR - The username cannot be null \n")
                continue
        elif option.casefold() == 'n':
            continue
        break

    while True:
        print("Insert your password: ")
        password = input().strip()
        print(f"Is '{password}' correct? [Y/n]")
        option = input()
        if option.casefold() == 'y':
            if password == "":
                print(" ERROR - The password cannot be null \n")
                continue
        elif option.casefold() == 'n':
            continue
        break

    connection.sendall((b'1-' + username.encode('utf-8') +
                        b'-' + password.encode('utf-8')))
    result = int(connection.recv(2).decode('utf-8'))  # LEGGI QUI PER CAPIRE COME RICEVERE DATI
    if result == 1:
        print("Error during the user creation.")
    elif result == 2:
        print("Username already in use, please choose another")
    else:
        print("User added succesfully")


def exit_connection(connection):
    connection.close()  # close the connection
    sys.exit()


def option_invalid():
    while True:
        print("Option not valid. Retry [Y/n]")
        select = input()

        if select.casefold() == 'y':
            return True
        elif select.casefold() == 'n':
            return False
