import asserDB
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os,sys

class MainClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        def cnt():
            akey = asserDB.readKeys(name=name.text())
            aval = asserDB.readVals(name=name.text())
            table.setRowCount(len(akey))
            for i in range(0,len(akey)):
                table.setItem(i,0,QTableWidgetItem(akey[i]))
                table.setItem(i,1,QTableWidgetItem(aval[i]))
    
        self.setWindowTitle('asserBrowser')
        name=QLineEdit(self)
        table=QTableWidget(self)
        table.setColumnCount(2)
        vbox=QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(table)
        self.setLayout(vbox)
        self.setGeometry(300,300,600,600)
        self.show()
        name.returnPressed.connect(lambda: cnt())
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    myWindow=MainClass()
    myWindow.show()
    app.exec_()
