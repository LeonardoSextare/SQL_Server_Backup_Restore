from PySide6.QtWidgets import QWizard
from .WelcomePage import WelcomePage
from .License import LicensePage
from .Installer import InstallPage
from .Finish import ConclusionPage
from .Configuration import ConfigurationPage

class InstallerWizard(QWizard):
    def __init__(self, model, controller, parent=None):
        super().__init__(parent)
        self.model = model
        self.controller = controller
        self.setWindowTitle("SQL Server Backup Restorer - Installer")
        self.setWizardStyle(QWizard.ModernStyle)

        # Adiciona as páginas do wizard
        self.addPage(WelcomePage())
        self.addPage(LicensePage(model, controller))
        self.addPage(ConfigurationPage(model, controller))
        self.addPage(InstallPage(model, controller))
        self.addPage(ConclusionPage())
