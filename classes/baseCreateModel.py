from classes.baseAutoHexaPy import BaseAutoHexaPy


class BaseCreateProject:
    def __init__(self):
        pass

    @staticmethod
    def get_available_attr():
        return {
            1: "AutoField",
            2: "IntegerField",
            3: "CharField",
            4: "TextField",
            5: "DateTimeField",
            6: "ForeignKey"
        }

    @staticmethod
    def tipo_auto_field():
        primary_key = input("¿Es primary key? (y/n): ")
        if primary_key == "y":
            return "AutoField(primary_key=True)"
        else:
            return "AutoField()"

    @staticmethod
    def tipo_integer_field():
        size = input("¿Tamaño del IntegerField? (default=11): ")
        if size == "":
            return "IntegerField()"
        else:
            return "IntegerField(max_length=" + size + ")"

    @staticmethod
    def tipo_char_field():
        size = input("¿Tamaño del CharField? (default=50): ")
        if size == "":
            return "CharField(max_length=50)"
        else:
            return "CharField(max_length=" + size + ")"

    @staticmethod
    def tipo_text_field():
        return "TextField()"

    @staticmethod
    def tipo_date_time_field():
        blank = input("¿Es blank? (y/n): ")
        null = input("¿Es null? (y/n): ")
        default = input("¿Default datetime.now? (y/n): ")
        string = ""
        if blank == "y":
            string += "blank=True, "
        if null == "y":
            string += "null=True, "
        if default == "y":
            string += "default=datetime.now"

        return "DateTimeField(blank=True, null=True, default=datetime.now)"

    @staticmethod
    def tipo_foreign_key(foreign_key_model):
        on_delete = input("¿Qué on_delete tiene? [CASCADE, SET_NULL...]: ")
        if on_delete == "":
            return "ForeignKey(" + foreign_key_model.title() + ")"
        else:
            return "ForeignKey(" + foreign_key_model.title() + ", on_delete=models." + on_delete + ")"

    @staticmethod
    def nombre_foreign_key():
        print("¿A qué modelo hace referencia?")
        for model in BaseAutoHexaPy().get_models():
            print(model)
        return input("Nombre del modelo: ").lower()
