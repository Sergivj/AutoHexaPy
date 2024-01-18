import fileinput
import os

from classes.configAutoHexaPy import ConfigAutoHexaPy


class BaseAutoHexaPy(ConfigAutoHexaPy):
    def __init__(self):
        super().__init__()

    @staticmethod
    def go_to_path():
        path = os.getcwd()
        path_list = path.split("AutoHexaPy")
        path = path_list[0] + "AutoHexaPy"
        os.chdir(path)
        return path

    def go_to_base_project_path(self):
        os.chdir(os.path.join(self.go_to_path(), self.nombre_proyecto))
        return os.getcwd()

    def go_to_project_path(self):
        os.chdir(os.path.join(self.go_to_base_project_path(), self.nombre_proyecto))
        return os.getcwd()

    def go_to_api_path(self, folder=""):
        if folder == "":
            os.chdir(os.path.join(self.go_to_base_project_path(), self.nombre_aplicacion))
        else:
            os.chdir(os.path.join(self.go_to_base_project_path(), self.nombre_aplicacion, folder))
        return os.getcwd()

    def migrations(self):
        self.go_to_base_project_path()
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")

    @staticmethod
    def create_folder(name_folder):
        os.system("mkdir " + name_folder)

    @staticmethod
    def create_file(name_file):
        os.system("touch " + name_file)

    @staticmethod
    def delete_file(name_file):
        os.system("rm " + name_file)

    @staticmethod
    def new_content(nombre_archivo, nuevo_contenido):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(nuevo_contenido)

    @staticmethod
    def write_endfile(nombre_archivo, nuevo_contenido):
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(nuevo_contenido)

    @staticmethod
    def replace_text(nombre_archivo, texto_a_buscar, texto_a_reemplazar):
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        contenido_modificado = contenido.replace(texto_a_buscar, texto_a_reemplazar)
        with open(nombre_archivo, 'w') as archivo_modificado:
            archivo_modificado.write(contenido_modificado)

    @staticmethod
    def add_content(ruta_archivo, linea_a_modificar, nuevo_contenido):
        with fileinput.FileInput(ruta_archivo, inplace=True, backup='.bak') as archivo:
            for linea in archivo:
                if linea.startswith(linea_a_modificar):
                    print(linea.strip() + f' {nuevo_contenido}')
                else:
                    print(linea, end='')

    @staticmethod
    def runserver():
        os.system("python manage.py runserver 25565")

    def get_models(self):
        self.go_to_api_path("domain/models")
        archivos_en_carpeta = os.listdir("")
        archivos = []
        for nombre_archivo in archivos_en_carpeta:
            if nombre_archivo.__contains__("model.py"):
                nombre_archivo = nombre_archivo.replace("_model.py", "")
                archivos.append(nombre_archivo)
        return archivos
