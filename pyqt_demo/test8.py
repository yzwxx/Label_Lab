#!/usr/bin/python
# -*- coding: utf-8 -*-



import os
from os.path import join
import sys
from PyQt4 import QtGui,QtCore


class FormWidget(QtGui.QWidget):
	def __init__(self):
		super(FormWidget, self).__init__()
		self.initUI()
		
	def initUI(self):  
		# print 'widget'
		model = QtGui.QStringListModel()
		model.setStringList(['some', 'words', 'in', 'my', 'dictionary','dict','SSR','interesting'])

		completer = QtGui.QCompleter()
		self.lineedit = QtGui.QLineEdit()
		completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
		completer.setModel(model)
		completer.activated.connect(self.printInfo)

		
		self.lineedit.setCompleter(completer)
		# self.lineedit.returnPressed.connect(self.printInfo)
		# lineedit.show()

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(self.lineedit)
		self.setLayout(vbox)

		
	def printInfo(self):
		self.lineedit.clear()
		print 'enter'

class MyMainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MyMainWindow, self).__init__()
		self.widget = FormWidget()
		self.setCentralWidget(self.widget) 
		self.setWindowTitle('Search Bar')
		self.setGeometry(300, 300, 350, 300)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)    
		self.show()


def main():
	app = QtGui.QApplication(sys.argv)
	foo = MyMainWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()