from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel


class WelcomePage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Bem-vindo ao Instalador do SQL Server Backup Restorer")
        description_str = "Esse script foi desenvolvido por Leonardo Sextare e seu codigo é aberto sobre a licensa MIT.\nPara mais informações sobre como utilizá-lo, visite o repositório oficial."
        description_label = QLabel(description_str)
        description_label.setWordWrap(True)
        
        repository_str = '<a href="https://github.com/usuario/meu-software">Leonardo Sextare - SQL Server Backup Restore</a>'
        repository_label = QLabel(repository_str)
        repository_label.setObjectName("Repositorio")

        layout = QVBoxLayout()
        layout.addWidget(description_label)
        layout.addWidget(repository_label)
        self.setLayout(layout)
