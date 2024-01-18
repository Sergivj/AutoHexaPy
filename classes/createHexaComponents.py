from classes.baseAutoHexaPy import BaseAutoHexaPy
import re


class CreateHexaComponents(BaseAutoHexaPy):
    def __init__(self, nombre_modelo, dict_atributos):
        super().__init__()
        self.nombre_modelo = nombre_modelo
        self.dict_atributos = dict_atributos

    def create_hexacomponents(self):
        CreateRepository(self.nombre_modelo).create_repository()
        CreateService(self.nombre_modelo).create_service()
        CreateViewset(self.nombre_modelo).create_viewset()
        CreateSerializer(self.nombre_modelo, self.dict_atributos).create_serializer()
        self.go_to_api_path()
        self.create_url()

    def get_nombre_modelo(self):
        for key in self.nombre_modelo:
            return key

    def create_url(self):
        nombre_modelo = self.get_nombre_modelo()

        self.add_content("urls.py", "router = DefaultRouter()",
                         "\nfrom " + self.nombre_aplicacion + ".infrastructure.viewsets." + nombre_modelo.lower() +
                         "_viewset import " + nombre_modelo.title() + "ViewSet" +
                         "\nrouter.register(r'" + nombre_modelo.lower() + "s', " + nombre_modelo.title() +
                         "ViewSet, basename='" + nombre_modelo.lower() + "s')")


class CreateRepository(BaseAutoHexaPy):
    def __init__(self, nombre_modelo):
        super().__init__()
        self.nombre_modelo = nombre_modelo
        self.go_to_api_path("domain/repositories")
        self.nombre_modelo = self.get_nombre_modelo()
        if self.nombre_modelo:
            self.create_file(self.nombre_modelo.lower() + "_repository.py")

    def get_nombre_modelo(self):
        for key in self.nombre_modelo:
            return key

    def create_repository(self):
        repository = ""
        repository += self.create_imports()
        repository += "\n"
        repository += self.create_class()
        repository += self.create_get_all()

        self.write_endfile(self.nombre_modelo.lower() + "_repository.py", repository)

    def create_imports(self):
        imports = ""
        imports += "from typing import Optional, List\n"
        imports += "from django.utils import timezone\n"
        imports += "from api_proyecto.domain.models." + self.nombre_modelo.lower() + "_model import " \
                   + self.nombre_modelo + "\n\n"
        return imports

    def create_class(self):
        return "class " + self.nombre_modelo.title() + "Repository:\n"

    def create_get_all(self):
        get_all = ""
        get_all += "    def get_all(self) -> List[" + self.nombre_modelo + "]:\n"
        get_all += "        return " + self.nombre_modelo + ".objects.all()\n\n"
        return get_all


class CreateService(BaseAutoHexaPy):
    def __init__(self, nombre_modelo):
        super().__init__()
        self.nombre_modelo = nombre_modelo
        self.go_to_api_path("application/services")
        self.nombre_modelo = self.get_nombre_modelo()
        if self.nombre_modelo:
            self.create_file(self.nombre_modelo.lower() + "_service.py")

    def get_nombre_modelo(self):
        for key in self.nombre_modelo:
            return key

    def create_service(self):
        service = ""
        service += self.create_imports()
        service += "\n"
        service += self.create_class()
        service += self.create_init()
        service += self.create_get_all()

        self.write_endfile(self.nombre_modelo.lower() + "_service.py", service)

    def create_imports(self):
        imports = ""
        imports += "from typing import Optional, List\n"
        imports += "from "+self.nombre_aplicacion+".domain.models." + self.nombre_modelo.lower() + "_model import " \
                   + self.nombre_modelo + "\n"
        imports += "from "+self.nombre_aplicacion+".domain.repositories." + self.nombre_modelo.lower() + \
                   "_repository import " + self.nombre_modelo + "Repository\n\n"
        return imports

    def create_class(self):
        return "class " + self.nombre_modelo.title() + "Service:\n"

    def create_init(self):
        init = ""
        init += "    def __init__(self):\n"
        init += "        self." + self.nombre_modelo.lower() + "_repository = " + self.nombre_modelo + \
                "Repository()\n\n"
        return init

    def create_get_all(self):
        get_all = ""
        get_all += "    def get_all(self) -> List[" + self.nombre_modelo + "]:\n"
        get_all += "        return self." + self.nombre_modelo.lower() + "_repository.get_all()\n\n"
        return get_all


class CreateSerializer(BaseAutoHexaPy):
    def __init__(self, nombre_modelo, dict_atributos):
        super().__init__()
        self.nombre_modelo = nombre_modelo
        self.dict_atributos = dict_atributos
        self.go_to_api_path("application/serializers")
        self.nombre_modelo = self.get_nombre_modelo()
        if self.nombre_modelo:
            self.create_file(self.nombre_modelo.lower() + "_serializer.py")

    def get_nombre_modelo(self):
        for key in self.nombre_modelo:
            return key

    def create_serializer(self):
        serializer = ""
        serializer += self.create_imports()
        serializer += "\n"
        serializer += self.create_class()
        serializer += self.create_attr()

        self.write_endfile(self.nombre_modelo.lower() + "_serializer.py", serializer)

    def create_imports(self):
        imports = ""
        imports += "from rest_framework import serializers\n\n"
        return imports

    def create_class(self):
        return "class " + self.nombre_modelo.title() + "Serializer(serializers.Serializer):\n"

    def create_attr(self):
        attr = ""
        for key in self.dict_atributos:
            line = self.dict_atributos[key]
            line = self.remove_parameters(line, "(", ")")

            line = line.replace("TextField", "CharField")
            line = line.replace("AutoField", "IntegerField")
            line = line.replace("ForeignKey", "CharField")

            attr += "    " + key + " = serializers." + line + "\n"
        return attr

    @staticmethod
    def remove_parameters(cadena, char_init, char_end):
        patron = re.compile(re.escape(char_init) + '.*?' + re.escape(char_end))
        resultado = patron.sub(char_init + char_end, cadena)
        return resultado


class CreateViewset(BaseAutoHexaPy):
    def __init__(self, nombre_modelo):
        super().__init__()
        self.nombre_modelo = nombre_modelo
        self.go_to_api_path("infrastructure/viewsets")
        self.nombre_modelo = self.get_nombre_modelo()
        if self.nombre_modelo:
            self.create_file(self.nombre_modelo.lower() + "_viewset.py")

    def get_nombre_modelo(self):
        for key in self.nombre_modelo:
            return key

    def create_viewset(self):
        viewset = ""
        viewset += self.create_imports()
        viewset += "\n"
        viewset += self.create_class()
        viewset += self.create_init()
        viewset += self.create_get_all()

        self.write_endfile(self.nombre_modelo.lower() + "_viewset.py", viewset)

    def create_imports(self):
        imports = ""
        imports += "from rest_framework import viewsets, status\n"
        imports += "from rest_framework.decorators import action\n"
        imports += "from rest_framework.permissions import IsAuthenticated\n"
        imports += "from rest_framework.response import Response\n"
        imports += "from rest_framework_simplejwt.tokens import RefreshToken\n\n"
        imports += "from "+self.nombre_aplicacion+".application.services." + self.nombre_modelo.lower() \
                   + "_service import " + self.nombre_modelo + "Service\n\n"
        imports += "from "+self.nombre_aplicacion+".application.serializers." + self.nombre_modelo.lower() \
                   + "_serializer import " + self.nombre_modelo.title() + "Serializer\n\n"

        return imports

    def create_class(self):
        clas = ""
        clas += "class " + self.nombre_modelo.title() + "ViewSet(viewsets.ModelViewSet):\n"
        clas += "    permission_classes = ()\n\n"
        return clas

    def create_init(self):
        init = ""
        init += "    def __init__(self, **kwargs):\n"
        init += "        super().__init__(**kwargs)\n"
        init += "        self.service = " + self.nombre_modelo + "Service()\n\n"
        return init

    def create_get_all(self):
        get_all = ""
        get_all += "    @action(detail=False, methods=['get'], url_path='get-all')\n"
        get_all += "    def get_all(self, request):\n"
        get_all += "        self.permission_classes = (IsAuthenticated,)\n"
        get_all += "        variable = self.service.get_all()\n\n"
        get_all += "        serializer = " + self.nombre_modelo + "Serializer(variable, many=True)\n\n"
        get_all += "        return Response(serializer.data)\n\n"
        return get_all
