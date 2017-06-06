#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
QMainWindow is a class that understands GUI elements like a
-toolbar,
-statusbar,
-central widget,
-docking areas.
QWidget is just a raw widget.

When you want to have a main window for you project, use QMainWindow and add the widget to it.
Remember to call setCentralWidget in QMainWindow and self.show() to show it.
'''


import os
from os.path import join
import sys
from PyQt4 import QtGui,QtCore

class FormWidget(QtGui.QWidget):
	def __init__(self):
		super(FormWidget, self).__init__()
		self.initUI()
		
	def initUI(self):  
		lcd = QtGui.QLCDNumber(self)
		sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)

		vbox = QtGui.QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display) # eventSource.eventObject.connect(eventTarget)
		


class MyMainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(MyMainWindow, self).__init__()
		self.widget = FormWidget()
		self.setCentralWidget(self.widget)
		self.setWindowTitle('Signal & slot')
		self.setGeometry(300, 300, 250, 150)
		self.show() 


def main():
	app = QtGui.QApplication(sys.argv)
	foo = MyMainWindow()
	#foo.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()