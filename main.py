# terminal command: pyuic5 gui.ui -o ../gui.py
import sys
from PyQt5 import QtWidgets
import gui
import pyvisa


class KeythleyApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # buttons connections
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label_2.setText('1234')


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    window = KeythleyApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    # run_app()
    rm = pyvisa.ResourceManager()
    print(rm.list_resources())
