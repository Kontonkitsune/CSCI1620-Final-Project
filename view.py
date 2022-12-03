# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BadCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(281, 290)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.ButtonCalc = QtWidgets.QPushButton(Dialog)
        self.ButtonCalc.setGeometry(QtCore.QRect(150, 220, 111, 51))
        self.ButtonCalc.setObjectName("ButtonCalc")
        self.ButtonClear = QtWidgets.QPushButton(Dialog)
        self.ButtonClear.setGeometry(QtCore.QRect(150, 160, 111, 51))
        self.ButtonClear.setObjectName("ButtonClear")
        self.LabelTitle = QtWidgets.QLabel(Dialog)
        self.LabelTitle.setGeometry(QtCore.QRect(40, 20, 201, 31))
        self.LabelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelTitle.setObjectName("LabelTitle")
        self.LabelResult = QtWidgets.QLabel(Dialog)
        self.LabelResult.setGeometry(QtCore.QRect(30, 110, 221, 41))
        self.LabelResult.setObjectName("LabelResult")
        self.ButtonPlus = QtWidgets.QPushButton(Dialog)
        self.ButtonPlus.setGeometry(QtCore.QRect(20, 160, 51, 51))
        self.ButtonPlus.setObjectName("ButtonPlus")
        self.ButtonMinus = QtWidgets.QPushButton(Dialog)
        self.ButtonMinus.setGeometry(QtCore.QRect(80, 160, 51, 51))
        self.ButtonMinus.setObjectName("ButtonMinus")
        self.ButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.ButtonMultiply.setGeometry(QtCore.QRect(20, 220, 51, 51))
        self.ButtonMultiply.setObjectName("ButtonMultiply")
        self.ButtonDivide = QtWidgets.QPushButton(Dialog)
        self.ButtonDivide.setGeometry(QtCore.QRect(80, 220, 51, 51))
        self.ButtonDivide.setObjectName("ButtonDivide")
        self.TextStorage = QtWidgets.QTextEdit(Dialog)
        self.TextStorage.setGeometry(QtCore.QRect(20, 60, 241, 41))
        self.TextStorage.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TextStorage.setObjectName("TextStorage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Test 10"))
        self.ButtonCalc.setText(_translate("Dialog", "Calculate"))
        self.ButtonClear.setText(_translate("Dialog", "Clear"))
        self.LabelTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Bad Calculator</span></p></body></html>"))
        self.LabelResult.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Whoops!</span></p></body></html>"))
        self.ButtonPlus.setText(_translate("Dialog", "+"))
        self.ButtonMinus.setText(_translate("Dialog", "-"))
        self.ButtonMultiply.setText(_translate("Dialog", "*"))
        self.ButtonDivide.setText(_translate("Dialog", "/"))
        self.TextStorage.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

