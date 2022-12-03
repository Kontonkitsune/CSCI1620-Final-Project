"""
Code by Lucian Reiter for CSCI1620
Dec 3, 2022
Code shamelessly ripped from Lab 10
"""

from PyQt5.QtWidgets import *
from view import *
import random


class Controller(QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.var1 = 0
        self.var2 = 0
        self.operation = "None"

        self.setupUi(self)

        self.setFixedSize(285, 432)

        self.ButtonCalc.clicked.connect(lambda: self.calculate())
        self.ButtonClear.clicked.connect(lambda: self.clearInputs())
        self.ButtonDivide.clicked.connect(lambda: self.division())
        self.ButtonMultiply.clicked.connect(lambda: self.multiplication())
        self.ButtonPlus.clicked.connect(lambda: self.addition())
        self.ButtonMinus.clicked.connect(lambda: self.subtraction())
        self.TextStorage.setText("")
        self.LabelResult.setText("")
        self.LabelResult.hide()

    def division(self):
        """Readies calculator for division."""
        self.var1 = self.TextStorage.toPlainText()
        self.LabelResult.setText(self.TextStorage.toPlainText() + " /")
        self.operation = "division"
        self.TextStorage.setText("")
        self.LabelResult.show()

    def addition(self):
        """Readies calculator for addition."""
        print("a")
        self.var1 = self.TextStorage.toPlainText()
        print("b")
        self.LabelResult.setText("%s +" % (self.TextStorage.toPlainText()))

        print("a")
        self.operation = "addition"

        print("b")
        self.TextStorage.setText("")

        print("a")
        self.LabelResult.show()

    def subtraction(self):
        """Readies calculator for subtraction."""
        self.var1 = self.TextStorage.toPlainText()
        self.LabelResult.setText(self.TextStorage.toPlainText() + " -")
        self.operation = "subtraction"
        self.TextStorage.setText("")
        self.LabelResult.show()

    def multiplication(self):
        """Readies calculator for multiplication."""
        self.var1 = self.TextStorage.toPlainText()
        self.LabelResult.setText(self.TextStorage.toPlainText() + " *")
        self.operation = "multiplication"
        self.TextStorage.setText("")
        self.LabelResult.show()

    def clearInputs(self):
        self.TextStorage.setText("")
        self.LabelResult.setText("")
        self.operation = "None"
        self.var1 = 0
        self.LabelResult.hide()

    def calculate(self):
        print("a")
        if self.operation == "None":
            self.TextStorage.setText("")
            self.LabelResult.setText("Something went wrong :(")
            self.LabelResult.show()

        else:
            try:
                var1 = float(self.var1)
                var2 = float(self.TextStorage.toPlainText())
                result = 0
                '''if random.randint(1,3) == 1:
                    raise ValueError
                if random.randint(1,20) == 1:
                    raise TypeError'''
                if self.operation == "addition":
                    result = var1 + var2
                    self.LabelResult.setText("%s + %s = " % (var1, var2))
                    self.TextStorage.setText(result)
                elif self.operation == "subtraction":
                    result = var1 - var2
                    self.LabelResult.setText("%s - %s = " % (var1, var2))
                    self.TextStorage.setText(result)
                elif self.operation == "multiplication":
                    result = var1 * var2
                    self.LabelResult.setText("%s * %s = " % (var1, var2))
                    self.TextStorage.setText(result)
                elif self.operation == "division":
                    result = var1 / var2
                    self.LabelResult.setText("%s / %s = " % (var1, var2))
                    self.TextStorage.setText(result)

            except ValueError:
                self.TextStorage.setText("")
                self.LabelResult.setText("Something went wrong :(")
                self.LabelResult.show()
                self.operation = "None"

            except TypeError:
                self.TextStorage.setText("")
                self.LabelResult.setText("Something went really wrong :(")
                self.LabelResult.show()
                self.operation = "None"



