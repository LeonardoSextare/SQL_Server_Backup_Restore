from PySide6.QtWidgets import QWizard
from .pages import *

class InstallerWizard(QWizard):
    def __init__(self, model, controller, parent=None):
        super().__init__(parent)
        self.model = model
        self.controller = controller
        self.setWindowTitle("SQL Server Backup Restorer - Installer")
        self.setWizardStyle(QWizard.ModernStyle)

        # Adiciona as páginas do wizard
        self.addPage(WelcomePage())
        self.addPage(ConfigurationPage(model, controller))
        self.addPage(InstallPage(model, controller))
        self.addPage(ConclusionPage())
