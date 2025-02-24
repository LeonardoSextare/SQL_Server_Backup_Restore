import sys
from PySide6.QtWidgets import QApplication
from AppContext import AppContext
from view import InstallerWizard

def main():
    app = QApplication(sys.argv)

    context = AppContext()
    wizard = InstallerWizard(context)
    
    wizard.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
