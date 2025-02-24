class ConfigurationController:
    def __init__(self, model):
        self.model = model

    def update_backup_storage_path(self, path: str) -> None:
        self.model.backup_storage_path = path

    def update_sql_instance(self, instance: str) -> None:
        self.model.sql_instance = instance

    def update_installation_path(self, path: str) -> None:
        self.model.installation_path = path
