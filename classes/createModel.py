from classes.baseAutoHexaPy import BaseAutoHexaPy
from classes.createHexaComponents import CreateHexaComponents


class CreateModel(BaseAutoHexaPy):
    def __init__(self, nombre_fichero, nombre_modelo, dict_imports, dict_atributos):
        super().__init__()
        self.nombre_fichero = nombre_fichero
        self.dict_nombre_modelo = nombre_modelo
        self.dict_imports = dict_imports
        self.dict_atributos = dict_atributos
        self.createHexaComponents = CreateHexaComponents(nombre_modelo, dict_atributos)

    def create_model(self, hexa=False):
        model = ""
        model += self.create_imports()
        model += self.create_model_name()
        model += self.create_attributes()
        model += "\n"
        self.new_content(self.nombre_fichero, model)
        if hexa:
            self.create_model_hexa()
        return model

    def create_model_hexa(self):
        self.createHexaComponents.create_hexacomponents()

    @staticmethod
    def create_from(libreria, clase):
        return "from " + libreria + " import " + clase + "\n"

    def create_imports(self):
        imports = ""
        for key in self.dict_imports:
            imports += self.create_from(key, self.dict_imports[key])
        return imports

    def create_model_name(self):
        model_name = ""
        for key in self.dict_nombre_modelo:
            model_name += "\n\nclass " + \
                     key + "(" + self.dict_nombre_modelo[key] + "):"
        return model_name

    def create_attributes(self):
        attributes = ""
        for key in self.dict_atributos:
            attributes += "\n    " + key + " = models." + self.dict_atributos[key]
        return attributes
