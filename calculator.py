# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(80, 190, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(140, 190, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(200, 190, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(80, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(140, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(200, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(80, 310, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(140, 310, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(200, 310, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btnY = QtWidgets.QPushButton(self.centralwidget)
        self.btnY.setGeometry(QtCore.QRect(80, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btnY.setFont(font)
        self.btnY.setStyleSheet("color: rgb(255, 0, 209);")
        self.btnY.setDefault(False)
        self.btnY.setObjectName("btnY")
        self.btnR = QtWidgets.QPushButton(self.centralwidget)
        self.btnR.setGeometry(QtCore.QRect(140, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btnR.setFont(font)
        self.btnR.setStyleSheet("color: rgb(255, 130, 5);")
        self.btnR.setObjectName("btnR")
        self.btnS = QtWidgets.QPushButton(self.centralwidget)
        self.btnS.setGeometry(QtCore.QRect(200, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btnS.setFont(font)
        self.btnS.setStyleSheet("color: rgb(55, 255, 0);")
        self.btnS.setObjectName("btnS")
        self.bntM = QtWidgets.QPushButton(self.centralwidget)
        self.bntM.setGeometry(QtCore.QRect(260, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.bntM.setFont(font)
        self.bntM.setStyleSheet("color: rgb(255, 0, 0);")
        self.bntM.setObjectName("bntM")
        self.btnP = QtWidgets.QPushButton(self.centralwidget)
        self.btnP.setGeometry(QtCore.QRect(260, 190, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btnP.setFont(font)
        self.btnP.setStyleSheet("color: rgb(0, 34, 255);")
        self.btnP.setObjectName("btnP")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(260, 310, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btnRA = QtWidgets.QPushButton(self.centralwidget)
        self.btnRA.setGeometry(QtCore.QRect(260, 250, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(20)
        self.btnRA.setFont(font)
        self.btnRA.setStyleSheet("color: rgb(255, 255, 20);\n"
"color: rgb(0, 85, 127);")
        self.btnRA.setObjectName("btnRA")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(80, 30, 241, 341))
        self.frame.setStyleSheet("background-color: rgb(144, 226, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 21))
        self.label.setStyleSheet("background-color: rgb(206, 222, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(4, 35, 231, 61))
        self.label_2.setStyleSheet("background-color: rgb(206, 222, 255);")
        self.label_2.setObjectName("label_2")
        self.frame.raise_()
        self.bntM.raise_()
        self.btn0.raise_()
        self.btn1.raise_()
        self.btn2.raise_()
        self.btn3.raise_()
        self.btn4.raise_()
        self.btn5.raise_()
        self.btn6.raise_()
        self.btn7.raise_()
        self.btn8.raise_()
        self.btn9.raise_()
        self.btnP.raise_()
        self.btnRA.raise_()
        self.btnS.raise_()
        self.btnY.raise_()
        self.btnR.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.calcul()
        self.ravnore = False

    def calcul(self):
           self.btn0.clicked.connect(lambda: self.write_n(self.btn0.text()))
           self.btn1.clicked.connect(lambda: self.write_n(self.btn1.text()))
           self.btn2.clicked.connect(lambda: self.write_n(self.btn2.text()))
           self.btn3.clicked.connect(lambda: self.write_n(self.btn3.text()))
           self.btn4.clicked.connect(lambda: self.write_n(self.btn4.text()))
           self.btn5.clicked.connect(lambda: self.write_n(self.btn5.text()))
           self.btn6.clicked.connect(lambda: self.write_n(self.btn6.text()))
           self.btn7.clicked.connect(lambda: self.write_n(self.btn7.text()))
           self.btn8.clicked.connect(lambda: self.write_n(self.btn8.text()))
           self.btn9.clicked.connect(lambda: self.write_n(self.btn9.text()))
           self.btnY.clicked.connect(lambda: self.write_n(self.btnY.text()))
           self.btnR.clicked.connect(lambda: self.write_n(self.btnR.text()))
           self.btnS.clicked.connect(lambda: self.write_n(self.btnS.text()))
           self.bntM.clicked.connect(lambda: self.write_n(self.bntM.text()))
           self.btnP.clicked.connect(lambda: self.write_n(self.btnP.text()))
           self.btnRA.clicked.connect(self.resultn)

    def resultn(self):
        res = eval(self.label_2.text())
        self.label_2.setText("=" + str(res))
        self.ravnore = True

    def write_n(self,number):
             if self.label_2.text() == "0" or self.ravnore:
                 self.label_2.setText(number)
                 self.ravnore = False
             else:
                 self.label_2.setText(self.label_2.text() + number)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnY.setText(_translate("MainWindow", "*"))
        self.btnR.setText(_translate("MainWindow", "/"))
        self.btnS.setText(_translate("MainWindow", "+"))
        self.bntM.setText(_translate("MainWindow", "-"))
        self.btnP.setText(_translate("MainWindow", "%"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnRA.setText(_translate("MainWindow", "="))
        self.label.setText(_translate("MainWindow", "Calculator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


