from classes.baseAutoHexaPy import BaseAutoHexaPy


class RewriteSettings(BaseAutoHexaPy):
    def __init__(self):
        super().__init__()

    def rewrite_auth_user_model(self):
        self.write_endfile("settings.py", f"\n\nAUTH_USER_MODEL = '{BaseAutoHexaPy().nombre_aplicacion}.User'")

    def rewrite_allowed_hosts(self):
        self.replace_text("settings.py", "ALLOWED_HOSTS = []", "ALLOWED_HOSTS = ['*']")

    def rewrite_installed_apps(self):
        self.add_content("settings.py",
                         "INSTALLED_APPS =", f"\n    '{BaseAutoHexaPy().nombre_aplicacion}',\n    'corsheaders',"
                                             f"\n    'rest_framework',\n    "
                                             f"'rest_framework_simplejwt.token_blacklist',")

    def rewrite_admin(self, reverse=False):
        if not reverse:
            self.replace_text('settings.py', "'django.contrib.admin'", "#'django.contrib.admin'")
        else:
            self.replace_text('settings.py', "#'django.contrib.admin'", "'django.contrib.admin'")

    def create_urls_api(self):
        self.go_to_api_path()
        self.create_file("urls.py")
        self.write_endfile("urls.py", "from django.urls import path, include\n"
                                      "from rest_framework.routers import DefaultRouter\n"
                                      "\n"
                                      "from . import views\n"
                                      "\n"
                                      "router = DefaultRouter()\n"
                                      "urlpatterns = [\n"
                                      "    path('', include(router.urls)),\n"
                                      "]\n")

    def rewrite_urls(self, reverse=False):
        self.go_to_project_path()
        if not reverse:
            self.replace_text("urls.py", "import path", "import path, include \n"
                                                        "from rest_framework_simplejwt import views as jwt_views")
            self.replace_text("urls.py", "path('admin/', admin.site.urls),", "#path('admin/', admin.site.urls),")
            self.write_endfile("urls.py", "\n    path('', include('" + self.nombre_aplicacion + ".urls')),")
            self.write_endfile("urls.py",
                               "    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),"
                               "\n")
            self.write_endfile("urls.py",
                               "    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),"
                               "\n")
            self.replace_text("urls.py", "]", "")
            self.write_endfile("urls.py", "]")
        else:
            self.replace_text("urls.py", "#path('admin/', admin.site.urls)", "path('admin/', admin.site.urls)\n")

    def rewrite_middleware(self):
        self.add_content("settings.py", "MIDDLEWARE =", f"\n    'corsheaders.middleware.CorsMiddleware',")

    def add_rest_framework(self):
        rest_variable = "REST_FRAMEWORK = {" \
                        "\n    'DEFAULT_AUTHENTICATION_CLASSES': [" \
                        "'rest_framework_simplejwt.authentication.JWTAuthentication'" \
                        "]" \
                        "\n}"
        self.write_endfile("settings.py", "\n\n"+rest_variable)

    def add_simple_jwt(self):
        simple_jwt_variable = "SIMPLE_JWT = {" \
                              "\n    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10)," \
                              "\n    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)," \
                              "\n    'ROTATE_REFRESH_TOKENS': True," \
                              "\n    'BLACKLIST_AFTER_ROTATION': True" \
                              "\n}"
        self.write_endfile("settings.py", "\n"+simple_jwt_variable)

    def add_import(self):
        self.add_content("settings.py", "from pathlib import Path", "\nfrom datetime import timedelta")
