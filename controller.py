"""
Code by Lucian Reiter for CSCI1620
Dec 3, 2022
Code shamelessly ripped from Lab 10
"""

from PyQt5.QtWidgets import *
from view import *
from functions import *
import random


class Controller(QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.var1 = None
        self.var2 = None
        self.var3 = None  # to store previous results.
        self.operation = None

        self.setupUi(self)

        self.setFixedSize(285, 432)

        self.ButtonCalc.clicked.connect(lambda: self.calculate(True))
        self.ButtonClear.clicked.connect(lambda: self.clearInputs())
        self.ButtonPlus.clicked.connect(lambda: self.update_calc_text("+"))
        self.ButtonMinus.clicked.connect(lambda: self.update_calc_text("-"))
        self.ButtonMultiply.clicked.connect(lambda: self.update_calc_text("*"))
        self.ButtonDivide.clicked.connect(lambda: self.update_calc_text("/"))
        self.TextStorage.setText("")
        self.LabelResult.setText("")
        self.LabelResult.hide()

    def update_calc_text(self, a: str) -> None:
        """Just updates the text stuff. Used with operation buttons."""
        if self.var1 is not None:
            self.calculate()
        self.operation = a
        print(a)
        self.var1 = self.TextStorage.toPlainText()
        self.var2 = None
        self.var3 = None
        self.LabelResult.setText(f"{simp(self.TextStorage.toPlainText())} {self.operation}")
        self.TextStorage.setText("")
        self.LabelResult.show()

    def clearInputs(self) -> None:
        """Clears inputs"""
        self.TextStorage.setText("")
        self.LabelResult.setText("")
        self.operation = None
        self.var1 = None
        self.var2 = None
        self.var3 = None
        self.LabelResult.hide()

    def calc_fail(self):
        self.TextStorage.setText("")
        self.LabelResult.setText("Something went really wrong :(")
        self.LabelResult.show()

    def calculate(self, standalone: bool = False) -> None:
        """
        Function does calculations based on self.operator, self.var1 and input from TextStorage
        Outputs the result of the calculation onto TextStorage, and the equation for the answer onto LabelResult

        :param standalone: Boolean. Whether the function is being run by the Calculate button or another button.
        :return: No return
        """

        if standalone:
            self.var2 = self.TextStorage.toPlainText() if self.var2 is None else self.var2
        else:
            self.var3 = None

        if self.operation is None:
            self.calc_fail()
        else:
            try:
                var1 = float(self.var3 if self.var3 is not None and standalone else self.var1)
                var2 = float(self.var2 if standalone else self.TextStorage.toPlainText())
                result = 0

                if random.randint(1, 5) == 1:  # program will occasionally act as though you input a string
                    raise ValueError

                if self.operation == "+":
                    result = var1 + var2
                elif self.operation == "-":
                    result = var1 - var2
                elif self.operation == "*":
                    result = var1 * var2
                elif self.operation == "/":
                    result = var1 / var2
                else:
                    raise TypeError  # simple way to exit loop

                self.LabelResult.setText(f"{simp(var1)} {self.operation} {simp(var2)} = "
                                         f"{simp(result)}")
                self.TextStorage.setText(simp(result))
                if standalone:
                    self.var3 = result
                    self.var1 = None

            except ValueError:
                try:
                    var1 = self.var3 if self.var3 is not None and standalone else self.var1
                    var2 = self.var2 if standalone else self.TextStorage.toPlainText()
                    result = 0

                    if self.operation == "+":
                        result = crazy_addition(var1, var2)  # literally tacks on the number to the string
                    elif self.operation == "-":
                        result = crazy_subtraction(var1, var2)
                    elif self.operation == "*":
                        result = crazy_multiplication(var1, var2)
                    elif self.operation == "/":
                        result = crazy_division(var1, var2)
                    else:
                        raise TypeError  # quick way to just end the code happening.

                    self.LabelResult.setText(f"{simp(var1)} {self.operation} {simp(var2)} = "
                                             f"{simp(result)}")
                    self.TextStorage.setText(simp(result))
                    if standalone:
                        self.var3 = result
                        self.var1 = None
                except ValueError:
                    self.calc_fail()
                except TypeError:
                    self.calc_fail()

            except TypeError:
                self.calc_fail()

            except ZeroDivisionError:
                var1 = self.var1
                var2 = self.TextStorage.toPlainText()
                self.LabelResult.setText(f"{simp(var1)} {self.operation} {simp(var2)} = "
                                         f"Undefined")
                self.TextStorage.setText("Undefined")
                self.LabelResult.show()
                self.operation = "None"
