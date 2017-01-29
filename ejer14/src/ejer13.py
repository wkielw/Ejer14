# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejer13.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(610, 547)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 30, 571, 441))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(460, 380, 75, 23))
        self.pushButton.setStyleSheet(_fromUtf8("border-radius: 5px,5px,5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.505, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 245, 243, 255));"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 521, 20))
        self.lineEdit.setStyleSheet(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 521, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(23, 110, 521, 261))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 610, 21))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMissatge = QtGui.QMenu(self.menubar)
        self.menuMissatge.setObjectName(_fromUtf8("menuMissatge"))
        self.menuMitssage = QtGui.QMenu(self.menubar)
        self.menuMitssage.setObjectName(_fromUtf8("menuMitssage"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionEsborra = QtGui.QAction(MainWindow)
        self.actionEsborra.setObjectName(_fromUtf8("actionEsborra"))
        self.actionEnvia = QtGui.QAction(MainWindow)
        self.actionEnvia.setObjectName(_fromUtf8("actionEnvia"))
        self.actionEsborrar = QtGui.QAction(MainWindow)
        self.actionEsborrar.setObjectName(_fromUtf8("actionEsborrar"))
        self.actionEnvia_2 = QtGui.QAction(MainWindow)
        self.actionEnvia_2.setObjectName(_fromUtf8("actionEnvia_2"))
        self.menuMissatge.addAction(self.actionEsborra)
        self.menuMitssage.addAction(self.actionEsborrar)
        self.menuMitssage.addAction(self.actionEnvia_2)
        self.menubar.addAction(self.menuMissatge.menuAction())
        self.menubar.addAction(self.menuMitssage.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.pushButton.setText(_translate("MainWindow", "Enviar...", None))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Insertar destinatario...", None))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Insertar asunto...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Missatge", None))
        self.menuMissatge.setTitle(_translate("MainWindow", "&Aplicacion", None))
        self.menuMitssage.setTitle(_translate("MainWindow", "Mitssage", None))
        self.actionEsborra.setText(_translate("MainWindow", "S&alir", None))
        self.actionEnvia.setText(_translate("MainWindow", "Envia", None))
        self.actionEsborrar.setText(_translate("MainWindow", "Esborrar", None))
        self.actionEnvia_2.setText(_translate("MainWindow", "Envia", None))
