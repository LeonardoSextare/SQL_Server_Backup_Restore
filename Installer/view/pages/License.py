from PySide6.QtWidgets import QWizardPage, QVBoxLayout, QLabel, QCheckBox


class LicensePage(QWizardPage):
    def __init__(self, model, controller, parent=None):
        super().__init__(parent)
        self.model = model
        self.controller = controller
        self.setTitle("Contrato de Licença")
        self.setSubTitle("Leia e aceite os termos para prosseguir.")

        license_text = (
            "Contrato de Licença de Software\n\n" "Leia atentamente os termos. Ao clicar em 'Avançar', " "você concorda com todos os termos estabelecidos."
        )
        label = QLabel(license_text)
        label.setWordWrap(True)

        self.checkbox = QCheckBox("Eu li e aceito os termos.")
        self.checkbox.stateChanged.connect(self.checkbox_changed)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

        # Sempre que o model alterar o estado de licenseAccepted,
        # notifica o wizard para atualizar o estado de completude da página.
        self.model.licenseAcceptedChanged.connect(lambda _: self.completeChanged.emit())

    def checkbox_changed(self, state):
        accepted = state == 2  # Qt.Checked tem valor 2
        # Atualiza o model via controller
        self.controller.set_license_accepted(accepted)

    def isComplete(self):
        # Permite avançar apenas se o usuário tiver aceitado os termos
        return self.model.licenseAccepted
