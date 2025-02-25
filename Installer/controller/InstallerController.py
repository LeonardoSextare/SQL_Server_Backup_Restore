from PySide6.QtCore import QTimer


class InstallerController:
    def __init__(self, model_installer, model_config):
        self.model_config = model_config
        self.model_installer = model_installer
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def set_license_accepted(self, accepted):
        self.model_config.licenseAccepted = accepted

    def start_installation(self):
        self.model_config.progress = 0
        self.timer.start(100) 

    def update_progress(self):
        self.model_config.increment_progress(5)
        if self.model_config.progress >= 100:
            self.timer.stop()
