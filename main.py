import sys
from os import sep
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from utils import CurrenciesConverter
from config import CURRENCY
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

        self.ui.inputCurrency.addItems(CURRENCY)
        self.ui.outputCurrency.addItems(CURRENCY)
        self.ui.inputAmount.setPlaceholderText('У меня есть: ')
        self.ui.outputAmount.setPlaceholderText('Я получу: ')

        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrenciesConverter()
        inputCurrency = self.ui.inputCurrency.currentText()
        outputCurrency = self.ui.outputCurrency.currentText()
        inputAmount = float(self.ui.inputAmount.text())

        outputAmount = c.convert(inputCurrency, outputCurrency, inputAmount)

        self.ui.outputAmount.setText(str(outputAmount))


app = QtWidgets.QApplication(sys.argv)
root = MoneyChanger()
root.show()

sys.exit(app.exec())


