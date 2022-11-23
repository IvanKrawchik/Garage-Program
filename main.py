import base_datos
from interfaz import login

def main():
    base_datos.init_db()
    login.login()

if __name__ == '__main__':
    main()