from classes.admin import Admin
from classes.createModel import CreateModel
from classes.baseAutoHexaPy import BaseAutoHexaPy
from classes.baseCreateModel import BaseCreateProject

# Crear archivos
BaseAutoHexaPy().go_to_api_path("domain/models")

nombre_modelo = input("Nombre del modelo: ").lower()
dict_imports = {
        "datetime": "datetime",
        "django.db": "models",
}

dict_atributos = {}


for i in range(int(input("¿Cuantos atributos tiene?"))):
    nombre_atributo = input("Nombre del atributo: ")
    tipo_atributo = input("Numero del atributo: "+str(BaseCreateProject().get_available_attr())+" ")
    if tipo_atributo == "1":
        dict_atributos[nombre_atributo] = BaseCreateProject().tipo_auto_field()
    elif tipo_atributo == "2":
        dict_atributos[nombre_atributo] = BaseCreateProject().tipo_integer_field()
    elif tipo_atributo == "3":
        dict_atributos[nombre_atributo] = BaseCreateProject().tipo_char_field()
    elif tipo_atributo == "4":
        dict_atributos[nombre_atributo] = BaseCreateProject().tipo_text_field()
    elif tipo_atributo == "5":
        dict_atributos[nombre_atributo] = BaseCreateProject().tipo_date_time_field()
    elif tipo_atributo == "6":
        foreign_key_model = BaseCreateProject().nombre_foreign_key()
        dict_imports["." + foreign_key_model + "_model"] = foreign_key_model.title()
        dict_atributos[nombre_atributo] = BaseCreateProject().tipo_foreign_key(foreign_key_model)


CreateModel(
    nombre_modelo+"_model.py",
    {nombre_modelo.title(): "models.Model"},
    dict_imports,
    dict_atributos
).create_model(hexa=True)

BaseAutoHexaPy().go_to_api_path()
BaseAutoHexaPy().write_endfile("models.py", f"from .domain.models." + nombre_modelo + "_model import "
                               + nombre_modelo.title() + " \n")

Admin().add_model_in_admin(nombre_modelo.title())

BaseAutoHexaPy().migrations()
