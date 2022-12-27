from hash import hash_string
import sys


def register_user(connection, username, password):
    hashed_password = hash_string(password)
    print(f"Hashed password: {hashed_password}")
    connection.sendall((b'1' +
                        '\xC6'.encode('utf-8') + username.encode('utf-8') +
                        '\xC6'.encode('utf-8') + password.encode('utf-8')))
    print("Now, bring the card close to the sensor.")
    result = int(connection.recv(1).decode('utf-8'))
    connection.recv(2)  # remove \r\n
    if result == 1:
        print("Error during the user registration.")
        return ""
    elif result == 2:
        print("Username already in use.")
        return ""
    else:
        print("User successfully created.")
        tag = connection.recv(30).decode('utf-8')
        connection.recv(2)  # remove \r\n
        return tag


def login_user(connection, username, password):
    hashed_password = hash_string(password)
    connection.sendall((b'2' +
                        '\xC6'.encode('utf-8') + username.encode('utf-8') +
                        '\xC6'.encode('utf-8') + password.encode('utf-8')))
    print("Now, bring the card close to the sensor.")
    result = int(connection.recv(1).decode('utf-8'))
    connection.recv(2)  # remove \r\n
    if result == 1:
        print("Error during the user login.")
        return ""
    elif result == 2:
        print("Username/Password not in memory.")
        return ""
    else:
        print("User logged succesfully.")
        tag = connection.recv(30).decode('utf-8')
        connection.recv(2)  # remove \r\n
        return tag


def add_credential(connection, username, password, tag):
    hashed_password = hash_string(password)
    print('\n --- Insert new credentials --- ')

    while True:
        print('Please insert Service Name: ')
        service_name = input().strip()
        if service_name == "":
            print(" ERROR - The name cannot be null \n")
            continue
        else:
            break

    while True:
        print('Please insert Service Password')
        service_password = input().strip()
        if service_password == "":
            print(" ERROR - The password cannot be null \n")
            continue
        else:
            break

    connection.sendall((b'3' +
                        '\xC6'.encode('utf-8') + username.encode('utf-8') +
                        '\xC6'.encode('utf-8') + password.encode('utf-8') +
                        '\xC6'.encode('utf-8') + tag.encode('utf-8') +
                        '\xC6'.encode('utf-8') + service_name.encode('utf-8') +
                        '\xC6'.encode('utf-8') + service_password.encode('utf-8')))
    result = int(connection.recv(1).decode('utf-8'))
    connection.recv(2)  # remove \r\n
    if result == 1:
        print("Something wrong happened, please try again.")
    else:
        print("Credentials successfully stored.")


def delete_credential(connection, username, password, tag):
    hashed_password = hash_string(password)
    print('\n --- Delete credentials --- ')

    while True:
        print('Please insert Service Name: ')
        service_name = input().strip()
        if service_name == "":
            print(" ERROR - The name cannot be null \n")
            continue
        else:
            break

    connection.sendall((b'4' +
                        '\xC6'.encode('utf-8') + username.encode('utf-8') +
                        '\xC6'.encode('utf-8') + hashed_password.encode('utf-8') +
                        '\xC6'.encode('utf-8') + tag.encode('utf-8') +
                        '\xC6'.encode('utf-8') + service_name.encode('utf-8')))
    result = int(connection.recv(1).decode('utf-8'))
    connection.recv(2)  # remove \r\n
    if result == 1:
        print("Something wrong happened, please try again.")
    else:
        print("Credentials successfully deleted.")


def view_credential(connection, username, password, tag):
    hashed_password = hash_string(password)
    print('\n --- View credentials --- ')

    while True:
        print('Please insert Service Name: ')
        service_name = input().strip()
        if service_name == "":
            print(" ERROR - The name cannot be null \n")
            continue
        else:
            break

    connection.sendall((b'5' +
                        '\xC6'.encode('utf-8') + username.encode('utf-8') +
                        '\xC6'.encode('utf-8') + password.encode('utf-8') +
                        '\xC6'.encode('utf-8') + tag.encode('utf-8') +
                        '\xC6'.encode('utf-8') + service_name.encode('utf-8')))
    result = int(connection.recv(1).decode('utf-8'))
    connection.recv(2)  # remove \r\n
    if result == 1:
        print("Something wrong happened, please try again.")
    else:
        cred = connection.recv(1024).decode('utf-8')
        connection.recv(2)  # remove \r\n
        print(f"The password for {service_name} is '{cred}'.")


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
