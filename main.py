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
        rm = pyvisa.ResourceManager()
        inst = rm.open_resource('GPIB0::07::INSTR')
        inst.query(":SENS:CHAN 2")
        # print(idn)
        # self.label_2.setText(str(idn))


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    window = KeythleyApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    run_app()

