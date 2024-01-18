from AutoHexaPy.classes.createModel import CreateModel
from AutoHexaPy.classes.admin import Admin
from AutoHexaPy.classes.rewriteSettings import RewriteSettings
from AutoHexaPy.classes.inicializeDjango import InicialiceDjango
from AutoHexaPy.classes.baseAutoHexaPy import BaseAutoHexaPy
from AutoHexaPy.classes.createSchedule import CreateSchedule

BaseAutoHexaPy().go_to_path()

# Inicializar Django
InicialiceDjango().install_django()

InicialiceDjango().start_project()
BaseAutoHexaPy().go_to_base_project_path()
InicialiceDjango().start_app()

BaseAutoHexaPy().migrations()

# Crear carpetas
BaseAutoHexaPy().go_to_api_path()
CreateSchedule().create_schedule()

BaseAutoHexaPy().go_to_project_path()

# Escribir en settings.py
RewriteSettings().rewrite_auth_user_model()
RewriteSettings().rewrite_allowed_hosts()
RewriteSettings().rewrite_installed_apps()
RewriteSettings().rewrite_admin()
RewriteSettings().rewrite_middleware()
RewriteSettings().add_rest_framework()
RewriteSettings().add_simple_jwt()
RewriteSettings().add_import()
RewriteSettings().create_urls_api()
RewriteSettings().rewrite_urls()

# Crear archivos
BaseAutoHexaPy().go_to_api_path("domain/models")

CreateModel(
    "user_model.py",
    {"User": "AbstractUser, models.Model"},
    {
        "django.contrib.auth.models": "AbstractUser",
        "django.db": "models"
    },
    {
        "username": "CharField(max_length=50, unique=True, blank=True)",
        "first_name": "CharField(max_length=50)",
        "last_name": "CharField(max_length=50)",
        "email": "EmailField(max_length=254, unique=True)",
        "password": "CharField(max_length=500)",
        "is_admin": "BooleanField(default=False)",
        "is_active": "BooleanField(default=True)",
        "is_staff": "BooleanField(default=False)",
        "is_superuser": "BooleanField(default=False)",
        "last_login": "DateTimeField(auto_now=True, blank=True, null=True)",
        "date_joined": "DateTimeField(blank=True, null=True, auto_now=True)"
    }
).create_model(hexa=True)

BaseAutoHexaPy().go_to_api_path()
CreateModel("models.py", {},
            {
                "django.db": "models",
                "api_proyecto.domain.models.user_model": "User"
            }, {}).create_model()

BaseAutoHexaPy().go_to_project_path()

# Pasamos las migraciones
BaseAutoHexaPy().migrations()

# Escribir en settings.py (otra vez para eliminar el comentario de admin)
BaseAutoHexaPy().go_to_project_path()
RewriteSettings().rewrite_admin(reverse=True)
RewriteSettings().rewrite_urls(reverse=True)

# Escribir en urls.py (otra vez para eliminar el comentario de admin)
BaseAutoHexaPy().replace_text("urls.py", "#path('admin/', admin.site.urls),", "path('admin/', admin.site.urls),")

# Creamos el modelo en Admin
BaseAutoHexaPy().go_to_base_project_path()
Admin().create_model_in_admin("User")

BaseAutoHexaPy().go_to_base_project_path()

# Borramos bd y creamos el super usuario
BaseAutoHexaPy().delete_file("db.sqlite3")
BaseAutoHexaPy().migrations()
Admin().create_super_user()

BaseAutoHexaPy().runserver()
