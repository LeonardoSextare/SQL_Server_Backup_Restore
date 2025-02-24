from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QComboBox, QFileDialog

class ConfigurationPage(QWizardPage):
    def __init__(self, context, parent=None):
        super().__init__(parent)
        self.context = context
        self.model = self.context.installer_model
        self.controller = self.context.installer_controller
        
        self.setTitle("Configuração")
        self.setSubTitle("Escolha o local de instalação, a instância do SQL Server e o local onde serão armazenadas as bases de dados restauradas")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Local de Instalação:"))
        self.install_path_line_edit = QLineEdit()
        self.install_path_line_edit.setText("C:/Program Files/SQL Backup Restorer")
        self.install_path_line_edit.setPlaceholderText("Selecione o local de instalação")
        self.install_path_line_edit.textChanged.connect(self.on_installation_path_changed)
        layout.addWidget(self.install_path_line_edit)

        layout.addWidget(QLabel("Local de Armazenamento das Bases Restauradas:"))
        path_layout = QHBoxLayout()
        self.storage_database_path_line_edit = QLineEdit()
        self.storage_database_path_line_edit.setPlaceholderText("Digite o caminho ou clique em 'Procurar...'")
        self.storage_database_path_line_edit.textChanged.connect(self.on_path_changed)
        path_layout.addWidget(self.storage_database_path_line_edit)
        layout.addLayout(path_layout)

        self.browse_button = QPushButton("Procurar...")
        self.browse_button.clicked.connect(self.browse_path)
        path_layout.addWidget(self.browse_button)

        layout.addWidget(QLabel("Instância do SQL Server:"))
        self.sql_instance_combo = QComboBox()
        self.sql_instance_combo.addItems(["MSSQLSERVER", "SQLEXPRESS", "SQL2019"])
        self.sql_instance_combo.currentIndexChanged.connect(self.on_sql_instance_changed)
        layout.addWidget(self.sql_instance_combo)

        self.setLayout(layout)

    def browse_path(self):
        directory = QFileDialog.getExistingDirectory(self, "Selecione o diretório")
        if directory:
            self.storage_database_path_line_edit.setText(directory)
            self.controller.update_backup_storage_path(directory)

    def on_path_changed(self, text):
        self.controller.update_backup_storage_path(text)
        self.completeChanged.emit()

    def on_installation_path_changed(self, text):
        self.controller.update_installation_path(text)
        self.completeChanged.emit()

    def on_sql_instance_changed(self, index):
        instance = self.sql_instance_combo.itemText(index)
        self.controller.update_sql_instance(instance)
        self.completeChanged.emit()

    def isComplete(self):
        return bool(self.model.installation_path) and bool(self.model.backup_storage_path) and bool(self.model.sql_instance)
