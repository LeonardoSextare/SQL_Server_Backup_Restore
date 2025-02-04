import sys
from PySide6.QtWidgets import QApplication
from sources import * 

def main():
    app = QApplication(sys.argv)

    model = InstallerModel()
    controller = InstallerController(model)
    wizard = InstallerWizard(model, controller)
    
    wizard.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
