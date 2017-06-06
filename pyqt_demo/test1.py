#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
a window with menu bar and tool bar
QAction with addAction for event handling(setting hot keys,showing status tip)
set window icon 
'''

import os
from os.path import join
import sys
from PyQt4 import QtGui,QtCore

icon_path = join(os.getcwd(),'icon.png')

class Example1(QtGui.QMainWindow):
	def __init__(self):
		super(Example1, self).__init__()
		self.initUI()

	def initUI(self):
		# text edit
		textEdit = QtGui.QTextEdit()
		self.setCentralWidget(textEdit)

		# menubar's action
		exitAction = QtGui.QAction('&Exit', self)        
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(QtGui.QApplication.quit)

		self.statusBar().showMessage('Ready')
		# menubar
		menubar = self.menuBar()
		menubar.setNativeMenuBar(False)
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction) # binding the action to the menu in menubar

		# toolbar
		self.toolbar = QtGui.QToolBar('name')
		self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
		self.toolbar.addAction(exitAction)
		self.addToolBar(QtCore.Qt.TopToolBarArea,self.toolbar)

		self.toolbar2 = QtGui.QToolBar('name')
		self.toolbar2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
		self.toolbar2.addAction(exitAction)
		self.addToolBar(QtCore.Qt.TopToolBarArea,self.toolbar2)
		


		self.setGeometry(500, 300, 550, 350) # set location of app windows on screen and its size
		self.setWindowTitle('GUI Demo')

		# window icon
		self.setWindowIcon(QtGui.QIcon(icon_path))

		# tooltip
		# QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		# self.setToolTip('This is a <b>QWidget</b> widget')
		
		# create buttons
		btn = QtGui.QPushButton('Button', self)
		# btn.setToolTip('This is a <b>QPushButton</b> widget')
		btn.resize(btn.sizeHint())
		btn.move(0, 300)

		qbtn = QtGui.QPushButton('Quit', self)
		qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(100, 300)

		# status bar
		# self.statusBar().showMessage('Ready')
		# self.statusBar().showMessage('not Ready')



		# center the window on screen
		self.center()
		self.show()

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 'Message',
			"Are you sure to quit?", QtGui.QMessageBox.Yes | 
				QtGui.QMessageBox.No, QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

def main():
	app = QtGui.QApplication(sys.argv) # Every PyQt4 application must create an application object
	#print sys.argv[1:]
	ex = Example1()
	sys.exit(app.exec_()) # The event handling starts from this point


if __name__ == '__main__':
    main()