# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QI_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 291, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Gilroy XBold")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Gilroy XBold")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Gilroy XBold")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_info = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(180, 70, 421, 71))
        self.txt_info.setObjectName("txt_info")
        self.txt_sign = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(180, 180, 421, 71))
        self.txt_sign.setObjectName("txt_sign")
        self.btn_gen_key = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_key.setGeometry(QtCore.QRect(430, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Gilroy Medium")
        font.setPointSize(15)
        self.btn_gen_key.setFont(font)
        self.btn_gen_key.setObjectName("btn_gen_key")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(20, 270, 171, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Gilroy Medium")
        font.setPointSize(15)
        self.btn_sign.setFont(font)
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(430, 270, 171, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Gilroy Medium")
        font.setPointSize(15)
        self.btn_verify.setFont(font)
        self.btn_verify.setObjectName("btn_verify")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Information"))
        self.label_3.setText(_translate("MainWindow", "Signature"))
        self.btn_gen_key.setText(_translate("MainWindow", "Generate key"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())