from PySide6.QtWidgets import QWizard
from .pages import *


class InstallerWizard(QWizard):
    def __init__(self, context, parent=None):
        super().__init__(parent)
        self.model = context

        self.setWindowTitle("SQL Server Backup Restorer - Installer")
        self.setWizardStyle(QWizard.ModernStyle)

        self.addPage(WelcomePage())
        self.addPage(ConfigurationPage(context))
        # self.addPage(InstallPage(context))
        self.addPage(ConclusionPage())
