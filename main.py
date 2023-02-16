import sys
from os import sep
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow


class MoneyChanger(QMainWindow):
    def __init__(self):
        super(MoneyChanger, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Money changer')
        self.setWindowIcon(QIcon('Pictures' + sep + 'change.png'))

        self.ui.inputCurrency.setPlaceholderText('Из валюты: ')
        self.ui.outputCurrency.setPlaceholderText('В валюту: ')
        self.ui.inputAmount.setPlaceholderText('У меня есть: ')
        self.ui.outputAmount.setPlaceholderText('Я получу: ')

        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        inputCurrency = self.ui.inputCurrency.text()
        outputCurrency = self.ui.outputCurrency.text()
        inputAmount = float(self.ui.inputAmount.text())

        outputAmount = round(c.convert(inputAmount, '%s' % inputCurrency, '%s' % outputCurrency), 2)

        self.ui.outputAmount.setText(str(outputAmount))


app = QtWidgets.QApplication(sys.argv)
root = MoneyChanger()
root.show()

sys.exit(app.exec())


