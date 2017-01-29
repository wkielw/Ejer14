# _*_ coding: utf-8 _*_

import sys
#import os
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtGui import *
from ejer13 import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        #Creacion de la barra de estado
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        #Creacion de los enlaces a las teclas del teclado
        self.shortcut_eviar = QtGui.QShortcut(self)
        self.shortcut_eviar.setKey(QtCore.Qt.CTRL + QtCore.Qt.Key_N)
        self.shortcut_eviar.activated.connect(self.enviar)
        
        self.shortcut_borrar = QtGui.QShortcut(self)
        self.shortcut_borrar.setKey(QtCore.Qt.CTRL + QtCore.Qt.Key_E)
        self.shortcut_borrar.activated.connect(self.borrar)
        
        self.shortcut_salir = QtGui.QShortcut(self)
        self.shortcut_salir.setKey(QtCore.Qt.CTRL + QtCore.Qt.Key_S)
        self.shortcut_salir.activated.connect(self.salir)
        
        
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.enviar)
        self.actionEnvia_2.triggered.connect(self.enviar)
        self.actionEsborrar.triggered.connect(self.borrar)
        self.actionEsborra.triggered.connect(self.salir)
       
        
    def enviar(self):
        self.statusBar.showMessage("Enviando....",1000)

    def borrar(self):
        self.statusBar.showMessage("Se han borrado los datos del formulario....",1000)
        self.lineEdit.setPlaceholderText("Inserte destinatario...")
        self.lineEdit_2.setPlaceholderText("Inserte asunto...")
        self.textEdit.setText("")
        
    def salir(self):
        sys.exit(app.exec_())
        
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
if __name__ == "__main__":

    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.center()
    ventana.show()

    sys.exit(app.exec_())        