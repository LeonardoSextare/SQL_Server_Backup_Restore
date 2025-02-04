from PySide6.QtCore import QTimer


class InstallerController:
    def __init__(self, model):
        self.model = model
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

    def set_license_accepted(self, accepted):
        self.model.licenseAccepted = accepted

    def start_installation(self):
        # Reinicia o progresso e inicia o timer para simular a instalação
        self.model.progress = 0
        self.timer.start(100)  # Atualiza a cada 100 ms

    def update_progress(self):
        self.model.increment_progress(5)
        if self.model.progress >= 100:
            self.timer.stop()