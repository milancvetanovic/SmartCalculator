import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from main_window_ui import Ui_MainWindow
from calculator import SmartCalculator


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
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
            self.resultDisplay.setText(result)
        else:
            self.resultDisplay.setText("Successful assignment")

        self.variablesDisplay.setText(self.calculator.dict_to_string(self.calculator.variables))

    def clearAllVariables(self):
        self.calculator.variables.clear()
        self.variablesDisplay.setText(self.calculator.dict_to_string(self.calculator.variables))

    def clearExpression(self):
        self.expressionEdit.clear()

    def keyPressEvent(self, event):
        if self.expressionEdit.hasFocus():
            if event.key() in (Qt.Key_Enter, Qt.Key_Return):
                if '=' in self.expressionEdit.text():
                    self.define_variable()
                else:
                    self.evaluate_expression()

    def connect_signals_slots(self):
        self.calcButton.clicked.connect(self.evaluate_expression)
        self.assignButton.clicked.connect(self.define_variable)
        self.clearVariableDisplay.clicked.connect(self.clearAllVariables)
        self.clearExpressionButton.clicked.connect(self.clearExpression)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    smart_calculator = QApplication([])
    win = Window()
    win.show()
    sys.exit(smart_calculator.exec())
