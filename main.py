import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem

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
            return None

        self.resultDisplay.setText("Successful assignment")
        self.expressionEdit.clear()
        self.refresh_variables(self.calculator.variables)

    def clearAllVariables(self):
        self.calculator.variables.clear()
        self.listWidget.clear()

    def clearExpression(self):
        self.expressionEdit.clear()

    def delSelectedVars(self):
        selected_vars = [item.text() for item in self.listWidget.selectedItems()]
        for var in selected_vars:
            var_key = [item.strip() for item in var.split('=')][0]
            self.calculator.variables.pop(var_key)

        self.refresh_variables(self.calculator.variables)

    def refresh_variables(self, var_list):
        self.listWidget.clear()
        for key, value in var_list.items():
            item = QListWidgetItem()
            item.setText(f"{key} = {value}")
            self.listWidget.addItem(item)

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
        self.clearExpressionButton.clicked.connect(self.clearExpression)
        self.clearVariableDisplay.clicked.connect(self.clearAllVariables)
        self.clearVariableButton.clicked.connect(self.delSelectedVars)


if __name__ == '__main__':
    smart_calculator = QApplication([])
    win = Window()
    win.show()
    sys.exit(smart_calculator.exec())
