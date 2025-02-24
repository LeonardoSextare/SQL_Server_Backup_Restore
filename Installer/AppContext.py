from model import *
from controller import *

class AppContext:
    def __init__(self):
        self.installer_model = InstallerModel()
        self.installer_controller = InstallerController(self.installer_model)
        
        self.configuration_model = ConfigurationModel()
        self.configuration_controller = ConfigurationController(self.configuration_model)
        
        # Outras dependências podem ser adicionadas aqui
