from classes.baseAutoHexaPy import BaseAutoHexaPy


class CreateSchedule(BaseAutoHexaPy):
    """
    Crea el siguiente schedule:

    proyecto
        application
            __init__.py
            use_cases
                __init__.py
            services
                __init__.py
            serializers
                __init__.py
        domain
            __init__.py
            models
                __init__.py
                user_model.py
            repositories
                __init__.py
        infrastructure
            __init__.py
            viewsets
                __init__.py
    """

    def __init__(self):
        super().__init__()

    def create_schedule(self):
        self.create_schedule_application()
        self.create_schedule_domain()
        self.create_schedule_infrastructure()

    def create_schedule_application(self):
        self.create_folder("application")
        self.create_file("application/__init__.py")

        self.create_folder("application/use_cases")
        self.create_file("application/use_cases/__init__.py")

        self.create_folder("application/services")
        self.create_file("application/services/__init__.py")

        self.create_folder("application/serializers")
        self.create_file("application/serializers/__init__.py")

    def create_schedule_domain(self):
        self.create_folder("domain")
        self.create_file("domain/__init__.py")

        self.create_folder("domain/models")
        self.create_file("domain/models/__init__.py")
        self.create_file("domain/models/user_model.py")

        self.create_folder("domain/repositories")
        self.create_file("domain/repositories/__init__.py")

    def create_schedule_infrastructure(self):
        self.create_folder("infrastructure")
        self.create_file("infrastructure/__init__.py")

        self.create_folder("infrastructure/viewsets")
        self.create_file("infrastructure/viewsets/__init__.py")
