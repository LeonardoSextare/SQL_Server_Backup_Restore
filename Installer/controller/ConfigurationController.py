class ConfigurationController:
    def __init__(self, model):
        self.model = model

    def get_sql_instances(self):
        return ["","MSSQLSERVER", "SQLEXPRESS", "SQL2019"]

    def update_backup_storage_path(self, path: str) -> None:
        self.model.backup_storage_path = path


    def update_sql_instance(self, instance: str) -> None:
        self.model.sql_instance = instance
        # print(self.model.sql_instance)

    def update_installation_path(self, path: str) -> None:
        self.model.installation_path = path
        # print(self.model.installation_path)
