# CRUD
# My project pharmacy

clients = 'Luis, Mateo,'.upper()


def create_client(cliente_name):
    global clients
    if client_name in clients:  # Si esta incluido
        print(f"{cliente_name} already exists")
    else:
        clients += client_name
        print(f"{clients} created")


def list_clients():
    global clients
    print(clients)


def _prin_welcome():
    print("Welcome to Pharmacy")
    print("="*50)
    print("What would you like to do today: ")
    print("[C] Create a User")
    print("[R] Read a User")
    print("[U] Update a User")
    print("[D] Delete a user")


def _get_user_():
    return input("Enter your name: ").upper()


if __name__ == '__main__':
    _prin_welcome()
    option = input("Enter your activity: ").upper()
    if option == "C":
        client_name = _get_user_()  # Se obtiene el nombre del cliente
        create_client(client_name)   # Se envía el nombre a la función
        list_clients()
    elif option == "R":
        client_name = _get_user_()
        list_clients()
    elif option == "U":
        client_name = _get_user_()
        list_clients()
    elif option == "D":
        client_name = _get_user_()
        list_clients()
    else:
        print("Invalid option")
