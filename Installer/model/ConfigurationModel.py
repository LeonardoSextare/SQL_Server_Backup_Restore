from PySide6.QtCore import QObject, Signal
import json


class ConfigurationModel(QObject):
    installation_path_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._installation_path = ""
        self._backup_storage_path = ""
        self._sql_instance = ""

    @property
    def backup_storage_path(self):
        return self._backup_storage_path

    @backup_storage_path.setter
    def backup_storage_path(self, value):
        if self._backup_storage_path != value:
            self._backup_storage_path = value

    @property
    def sql_instance(self):
        return self._sql_instance

    @sql_instance.setter
    def sql_instance(self, value):
        if self._sql_instance != value:
            self._sql_instance = value

    @property
    def installation_path(self):
        return self._installation_path

    @installation_path.setter
    def installation_path(self, value):
        if self._installation_path != value:
            self._installation_path = value
            self.installation_path_signal.emit(value)

    def save_config_to_json(self, filename="config.json"):
        config = {"installation_path": self.installation_path, "backup_storage_path": self.backup_storage_path, "sql_instance": self.sql_instance}
        with open(filename, "w") as f:
            json.dump(config, f, indent=4)
        print(f"Configuração salva em {filename}")
