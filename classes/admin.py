import os

from classes.baseAutoHexaPy import BaseAutoHexaPy


class Admin(BaseAutoHexaPy):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_super_user(username="admin", email="admin@admin.com", password="adminpass"):
        os.system("DJANGO_SUPERUSER_USERNAME=" + username + " DJANGO_SUPERUSER_PASSWORD=" + password +
                  " DJANGO_SUPERUSER_EMAIL=" + email + " python manage.py createsuperuser --noinput")

    def create_model_in_admin(self, nombre_modelo):
        self.go_to_api_path()
        self.write_endfile("admin.py", f"from django.contrib import admin\n\nfrom .models "
                                       f"import {nombre_modelo}\n\nadmin.site.register({nombre_modelo})")

    def add_model_in_admin(self, nombre_modelo):
        self.go_to_api_path()
        self.replace_text("admin.py", "from .models import ", f"from .models import {nombre_modelo}, ")
        self.write_endfile("admin.py", f"\nadmin.site.register({nombre_modelo})")
