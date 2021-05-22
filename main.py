import sys

from PyQt5.QtWidgets import QApplication

from Ui import UI

if __name__ == '__main__':
    App = QApplication(sys.argv)

    print("start")
    sys._excepthook = sys.excepthook


    def exception_hook(exctype, value, traceback):
        print(exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)
        sys.exit(1)


    sys.excepthook = exception_hook


    window = UI()
    window.show()

    sys.exit(App.exec())
