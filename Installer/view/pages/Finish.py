from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel


class ConclusionPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Conclusão")
        label = QLabel("A instalação foi concluída com sucesso!")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
