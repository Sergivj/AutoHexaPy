import os
import sys


def main():
    # El primer elemento de sys.argv es el nombre del script
    if len(sys.argv) != 2:
        print("No se han pasado argumentos correctamente")
        return

    # Los argumentos se encuentran a partir del segundo elemento
    function = sys.argv[1] if len(sys.argv) > 1 else None

    if function == "new-project":
        os.system("python3 autohexapy_new_project.py")
    elif function == "create-model":
        os.system("python3 autohexapy_create_model.py")

    else:
        print("No se ha encontrado la función")
        return


if __name__ == "__main__":
    main()
