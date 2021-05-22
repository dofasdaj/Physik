import sys

from PyQt5.QtWidgets import QApplication

from Ui import UI

if __name__ == '__main__':
    App = QApplication(sys.argv)

    window = UI()
    window.show()

    sys.exit(App.exec())
