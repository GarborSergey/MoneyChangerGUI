import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow


class MoneyChanger(QMainWindow, Ui_MainWindow):
    def __int__(self):
        super(MoneyChanger, self).__init__()
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())


