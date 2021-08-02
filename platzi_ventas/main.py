"""
Main file for Platzi Ventas
Author: Andres Gutierrez Arcia
june 2019
"""


import csv
import os


CLIENT_TABLE = r'platzi_ventas\clients.csv'
CLIENT_SCHEMA = ['name','company','email','position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)



def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f,fieldname=CLIENT_SCHEMA)
        writer.writerow(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client_name):
    global clients

    clients += client_name
    _add_comma()


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ','


def _print_welcome():
    print("Welcome")
    print(50 * "*")
    print("What do you want to do?")
    print("[C] Create client")
    print("[D] Delete client")


if __name__ == "__main__":
    _initialize_clients_from_storage()
    _print_welcome()
    # Get input
    # some logic
    # end, save files
    _save_clients_to_storage()

