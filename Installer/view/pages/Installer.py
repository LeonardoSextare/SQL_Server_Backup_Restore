from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QProgressBar


class InstallPage(QWizardPage):
    def __init__(self, model, controller, parent=None):
        super().__init__(parent)
        self.model = model
        self.controller = controller
        self.setTitle("Instalação")
        self.setSubTitle("A instalação está em andamento. Por favor, aguarde...")

        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(self.model.progress)

        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

        # Atualiza a barra de progresso conforme o model emitir o sinal progressChanged
        self.model.progressChanged.connect(self.progressBar.setValue)
        self.model.progressChanged.connect(lambda _: self.completeChanged.emit())

        def initializePage(self):
            # Quando a página é exibida, inicia o processo de instalação
            self.controller.start_installation()

        def isComplete(self):
            # Permite avançar apenas quando o progresso atingir 100%
            return self.model.progress >= 100
