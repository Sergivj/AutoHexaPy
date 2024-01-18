import os

from classes.baseAutoHexaPy import BaseAutoHexaPy


class InicialiceDjango(BaseAutoHexaPy):
    def __init__(self):
        super().__init__()

    def install_django(self):
        os.system("pip install django")
        os.system("pip install django-cors-headers")
        os.system("pip install djangorestframework")
        os.system("pip install djangorestframework-simplejwt==5.3.0")

    def start_project(self):
        os.system("django-admin startproject " + self.nombre_proyecto)

    def start_app(self):
        os.system("django-admin startapp " + self.nombre_aplicacion)

