#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join
import sys
from PyQt4 import QtGui,QtCore

'''
dialogs
'''

# class Example(QtGui.QMainWindow):
# 	def __init__(self):
# 		super(Example, self).__init__()
# 		self.initUI()

# 	def initUI(self):      
# 		self.btn = QtGui.QPushButton('Dialog', self)
# 		self.btn.move(20, 20)
# 		self.btn.clicked.connect(self.showDialog)
		
# 		self.le = QtGui.QLineEdit(self)
# 		self.le.move(130, 20)

# 		self.setGeometry(300, 300, 290, 150)
# 		self.setWindowTitle('Input dialog')
# 		self.show()
		
# 	def showDialog(self):
# 		text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
# 			'Enter your name:')
		
# 		if ok:
# 			self.le.setText(str(text))

# class Example(QtGui.QWidget):
    
#     def __init__(self):
#         super(Example, self).__init__()
        
#         self.initUI()
        
#     def initUI(self):      

#         vbox = QtGui.QVBoxLayout()

#         btn = QtGui.QPushButton('Dialog', self)
#         btn.setSizePolicy(QtGui.QSizePolicy.Fixed,
#             QtGui.QSizePolicy.Fixed)
#         btn.move(20, 20)
#         vbox.addWidget(btn)
#         btn.clicked.connect(self.showDialog)
        
#         self.lbl = QtGui.QLabel('Knowledge only matters', self)
#         self.lbl.move(130, 20)

#         vbox.addWidget(self.lbl)
#         self.setLayout(vbox)          
        
#         QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)

#         self.setGeometry(300, 300, 250, 180)
#         self.setWindowTitle('Font dialog')
#         self.show()
        
#     def showDialog(self):
#         font, ok = QtGui.QFontDialog.getFont()
#         if ok:
#             self.lbl.setFont(font)

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        openFile = QtGui.QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)   
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)    

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def showDialog(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')
        
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.textEdit.setText(data)


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()