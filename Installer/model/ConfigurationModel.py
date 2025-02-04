from PySide6.QtCore import QObject, Signal
import json

class InstallerModel(QObject):
    # Sinais para notificar alterações de estado (ex.: progresso e aceitação do contrato)
    progressChanged = Signal(int)
    licenseAcceptedChanged = Signal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._progress = 0
        self._licenseAccepted = False
        self._backup_storage_path = ""
        self._sql_instance = ""

    # Propriedade para o progresso da instalação.
    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if self._progress != value:
            self._progress = value
            self.progressChanged.emit(value)

    # Propriedade para o aceite do contrato de licença.
    @property
    def licenseAccepted(self):
        return self._licenseAccepted

    @licenseAccepted.setter
    def licenseAccepted(self, value):
        if self._licenseAccepted != value:
            self._licenseAccepted = value
            self.licenseAcceptedChanged.emit(value)
            
    # Propriedade para o caminho onde os backups serão armazenados.
    @property
    def backup_storage_path(self):
        return self._backup_storage_path

    @backup_storage_path.setter
    def backup_storage_path(self, value):
        if self._backup_storage_path != value:
            self._backup_storage_path = value

    # Propriedade para a instância selecionada do SQL Server.
    @property
    def sql_instance(self):
        return self._sql_instance

    @sql_instance.setter
    def sql_instance(self, value):
        if self._sql_instance != value:
            self._sql_instance = value

    def increment_progress(self, increment=5):
        self.progress = min(self.progress + increment, 100)

    def save_config_to_json(self, filename="config.json"):
        config = {
            "backup_storage_path": self.backup_storage_path,
            "sql_instance": self.sql_instance
        }
        with open(filename, "w") as f:
            json.dump(config, f, indent=4)
            print(f"Configuração salva em {filename}")
