#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join
import sys
from PyQt4 import QtGui,QtCore

'''
create self-defined event handler buttonClicked
overload event handler mousePressEvent
self-define signal,emit it in overloaded event and bind it with event handler
'''

# create a new signal closeApp, which is emitted during a mouse press event
class Communucation(QtCore.QObject): 
	closeApp = QtCore.pyqtSignal()


class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):      
		btn1 = QtGui.QPushButton("button 1", self)
		btn1.move(30, 50)

		btn2 = QtGui.QPushButton("Button 2", self)
		btn2.move(150, 50)
		
		btn1.clicked.connect(self.buttonClicked)            
		btn2.clicked.connect(self.buttonClicked)
		
		self.statusBar()

		self.c = Communucation()
		# The custom closeApp signal is connected to the close() slot of the QtGui.QMainWindow
		self.c.closeApp.connect(self.close)
		
		self.setGeometry(300, 300, 290, 150)
		self.setWindowTitle('Event sender')
		self.show()
		
	def buttonClicked(self): # event handler
		sender = self.sender()
		print sender.text() # the text of QPushButton
		self.statusBar().showMessage(sender.text() + ' was pressed')

	def mousePressEvent(self,event): # overwrite the event that emits the clossApp signal
		self.c.closeApp.emit()


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()