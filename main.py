import base_datos
from interfaz.login import login

def main():
    base_datos.init_db()
    login()

if __name__ == '__main__':
    main()