import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from main_window_ui import Ui_MainWindow
from calculator import SmartCalculator


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.calculator = SmartCalculator()
        self.connect_signals_slots()

    def evaluate_expression(self):
        expression = self.expressionEdit.text()
        result = self.calculator.handle_expression(expression)
        self.resultDisplay.setText(result)

    def define_variable(self):
        expression = self.expressionEdit.text()
        result = self.calculator.assignment(expression)
        if result:
            print(result)
            self.resultDisplay.setText(result)
        else:
            self.resultDisplay.setText("Successful assignment")

        print(self.calculator.variables)
        # Find a way to print variables in variablesDisplay field
        # each variable shall be printed in new line in format name = value

    def connect_signals_slots(self):
        self.calcButton.clicked.connect(self.evaluate_expression)
        self.assignButton.clicked.connect(self.define_variable)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    smart_calculator = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(smart_calculator.exec())
