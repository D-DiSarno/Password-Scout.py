import ssl
from socket import socket, AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER
from Loader import *
from main import select_actions
import netifaces


def get_ip():
    for iface in netifaces.interfaces():
        iface_details = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in iface_details:
            for ip_interfaces in iface_details[netifaces.AF_INET]:
                for key1, ip_add in ip_interfaces.items():
                    if key1 == 'addr' and ip_add != '127.0.0.1':
                        return ip_add


def init_server():
    loader = Loader("Loading Esp32 connection...", "Done!", 0.05).start()
    ip = get_ip()
    port = 11111
    context = SSLContext(PROTOCOL_TLS_SERVER)

    context.load_cert_chain("certs/server/domain.pem", "certs/server/domainK.pem")

    # client authentication
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations("certs/CA/rootCA.pem")

    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind((ip, port))
        server.listen(1)
        with context.wrap_socket(server, server_side=True) as tls:
            connection, address = tls.accept()
            loader.stop()
            print(f'Connected by {address}')
            select_actions(connection)
