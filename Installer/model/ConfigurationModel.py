from PySide6.QtCore import QObject, Signal


class ConfigurationModel(QObject):
    installation_path_signal = Signal(str)
    backup_storage_path_changed = Signal(str)
    sql_instance_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._installation_path = "C:/Program Files/SQL Backup Restorer"
        self._backup_storage_path = "C:/Program Files/SQL Backup Restorer/Bases Restauradas"
        self._sql_instance = ""

    @property
    def installation_path(self):
        return self._installation_path

    @installation_path.setter
    def installation_path(self, value):
        if self._installation_path != value:
            self._installation_path = value
            self.installation_path_signal.emit(value)

    @property
    def backup_storage_path(self):
        return self._backup_storage_path

    @backup_storage_path.setter
    def backup_storage_path(self, value):
        if self._backup_storage_path != value:
            self._backup_storage_path = value
            self.backup_storage_path_changed.emit(value)

    @property
    def sql_instance(self):
        return self._sql_instance

    @sql_instance.setter
    def sql_instance(self, value):
        if self._sql_instance != value:
            self._sql_instance = value
            self.sql_instance_changed.emit(value)
