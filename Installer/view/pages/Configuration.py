from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QComboBox, QFileDialog


class ConfigurationPage(QWizardPage):
    def __init__(self, model, controller, parent=None):
        super().__init__(parent)
        self.model = model
        self.controller = controller
        self.setTitle("Configuração")
        self.setSubTitle("Configure o caminho para armazenar os backups restaurados e selecione a instância do SQL Server.")

        # Campo para o caminho de armazenamento (com opção de digitar manualmente ou usar o botão de busca)
        self.path_line_edit = QLineEdit()
        self.path_line_edit.setPlaceholderText("Digite o caminho ou clique em 'Procurar...'")
        self.path_line_edit.textChanged.connect(self.on_path_changed)

        self.browse_button = QPushButton("Procurar...")
        self.browse_button.clicked.connect(self.browse_path)

        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_line_edit)
        path_layout.addWidget(self.browse_button)

        # Campo para selecionar a instância do SQL Server
        self.sql_instance_combo = QComboBox()
        self.sql_instance_combo.addItems(["MSSQLSERVER", "SQLEXPRESS", "SQL2019"]) # Placeholder, fazer a função real mais tarde
        self.sql_instance_combo.currentIndexChanged.connect(self.on_sql_instance_changed)

        # Layout principal
        layout = QVBoxLayout()
        layout.addLayout(path_layout)
        layout.addWidget(QLabel("Selecione a instância do SQL Server:"))
        layout.addWidget(self.sql_instance_combo)
        self.setLayout(layout)

    def browse_path(self):
        # Abre o diálogo para seleção de diretório
        directory = QFileDialog.getExistingDirectory(self, "Selecione o diretório")
        if directory:
            self.path_line_edit.setText(directory)
            self.controller.update_backup_storage_path(directory)

    def on_path_changed(self, text):
        self.controller.update_backup_storage_path(text)
        self.completeChanged.emit()

    def on_sql_instance_changed(self, index):
        instance = self.sql_instance_combo.itemText(index)
        self.controller.update_sql_instance(instance)
        self.completeChanged.emit()

    def isComplete(self):
        # Permite avançar somente se os dois campos estiverem preenchidos
        return bool(self.model.backup_storage_path) and bool(self.model.sql_instance)