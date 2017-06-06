#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
to improve: 
rearrange the layout
an instruction for using this tool
current just suitable for jpeg,png images no other choice available
current version doesn't support correcting labels after saving them(done)
smart tip(done)
click on label button to change text

author: zhongwei
date: 3rd June,2017
'''
import sys
from PyQt4 import QtGui,QtCore
from os import listdir,getcwd
from os.path import isfile,join
import json


__appname__ = 'Label_Lab'

class MyWidget(QtGui.QWidget):
	def __init__(self,parent=None):
		super(MyWidget, self).__init__(parent)
		self.curImgIndex = None
		self.MaxImgIndex = None
		self.inputFilePath = ''
		self.outputFile = ''
		self.initWidget()

	def initWidget(self):
		####################
		##   left widget  ##
		####################

		# buttons
		self.btn1 = QtGui.QPushButton('Open', self)
		self.btn1.setFixedSize(70,40)
		self.btn2 = QtGui.QPushButton('Output', self)
		self.btn2.setFixedSize(70,40)		
		self.btn3 = QtGui.QPushButton('Previous', self)
		self.btn3.setFixedSize(70,40)		
		self.btn4 = QtGui.QPushButton('Next', self)
		self.btn4.setFixedSize(70,40)
		self.btn5 = QtGui.QPushButton('Save', self)
		self.btn5.setFixedSize(70,40)
		# self.btn6 = QtGui.QPushButton('Discard', self)
		# self.btn6.setFixedSize(70,40)

		# shortcuts
		# set input file path
		QtGui.QShortcut(QtGui.QKeySequence("Alt+1"), self, self.inputFileDialog)
		# set output file path
		QtGui.QShortcut(QtGui.QKeySequence("Alt+2"), self, self.outputFileDialog)
		# refresh the QLineEdit
		QtGui.QShortcut(QtGui.QKeySequence("Alt+3"), self, self.cleanLineEdit)
		# show previous image
		QtGui.QShortcut(QtGui.QKeySequence("Alt+a"), self, self.showPrevImg)
		# show next image
		QtGui.QShortcut(QtGui.QKeySequence("Alt+d"), self, self.showNextImg)
		# save the labels for current image to output file
		QtGui.QShortcut(QtGui.QKeySequence("Alt+s"), self, self.saveLabels)
		# discard current image from input file
		# QtGui.QShortcut(QtGui.QKeySequence("Alt+z"), self, self.discardImg)


		# bingding event handler with buttons
		self.btn1.clicked.connect(self.inputFileDialog)
		self.btn2.clicked.connect(self.outputFileDialog)
		self.btn3.clicked.connect(self.showPrevImg)
		self.btn4.clicked.connect(self.showNextImg)
		self.btn5.clicked.connect(self.saveLabels)
		# self.btn6.clicked.connect(self.discardImg)

		# grid layout
		self.leftLayout = QtGui.QGridLayout()
		self.leftLayout.setSpacing(10)
		self.leftLayout.addWidget(self.btn1,1,0)
		self.leftLayout.addWidget(self.btn2,2,0)
		self.leftLayout.addWidget(self.btn3,3,0)
		self.leftLayout.addWidget(self.btn4,4,0)
		self.leftLayout.addWidget(self.btn5,5,0)
		# self.leftLayout.addWidget(self.btn6,6,0)


		####################
		##   mid widget   ##
		####################
		# display images for labelling
		self.imgLabel = QtGui.QLabel(self)
		pixmap = QtGui.QPixmap('start.png')
		self.imgLabel.setPixmap(pixmap)

		self.midLayout = QtGui.QVBoxLayout()
		self.midLayout.addWidget(self.imgLabel)

		####################
		##   right widget ##
		####################
		self.inputFileLabel = QtGui.QLabel('Input File: ',self)
		self.outputFileLabel = QtGui.QLabel('Output File: ',self)

		# a set for all labels created so far
		self.labelSet = list() # each time it should be loaded from result.jl

		# model for search bar completer
		self.tagEditor = QtGui.QLineEdit(self)
		self.tagEditorCompleter = QtGui.QCompleter(self)
		self.tagEditorModel = QtGui.QStringListModel(self)
		

		self.tagEditorModel.setStringList(self.labelSet)
		self.tagEditorCompleter.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
		self.tagEditorCompleter.setModel(self.tagEditorModel)

		self.tagEditor.setCompleter(self.tagEditorCompleter)
		self.tagEditor.setFixedWidth(70) # input string length constraint
		self.tagEditor.textEdited.connect(self.setEditorWidth) # make the length of editor adjustable to input
		self.tagEditor.returnPressed.connect(self.createLabel)

		# a list containing these temp widgets to be removed later
		self.tempWigdets = list()

		self.tagLayout = QtGui.QVBoxLayout()
		self.tagLayout.addWidget(self.tagEditor)
		self.tagLayout.addStretch(1)

		self.rightLayout = QtGui.QVBoxLayout()
		self.rightLayout.addWidget(self.inputFileLabel)
		self.rightLayout.addWidget(self.outputFileLabel)
		self.rightLayout.addLayout(self.tagLayout)
		self.rightLayout.addStretch(1)


		####################
		##   up widget    ##
		####################
		# up widget is the combination of left,mid and right widgets
		self.upLayout = QtGui.QHBoxLayout()
		self.upLayout.addLayout(self.leftLayout)
		self.upLayout.addStretch(1)
		self.upLayout.addLayout(self.midLayout)
		self.upLayout.addStretch(1)
		self.upLayout.addLayout(self.rightLayout)

		####################
		##   main widget  ##
		####################
		self.mainLayout = QtGui.QVBoxLayout()
		self.mainLayout.addLayout(self.upLayout)
		# to show the work progress
		self.progressBar = QtGui.QStatusBar()
		self.mainLayout.addWidget(self.progressBar)

		self.setLayout(self.mainLayout)

	def cleanLineEdit(self):
		'''
		clear the tag editor
		'''
		self.tagEditor.clear()

	def createLabel(self):
		'''
		create labels from the tag editor
		'''
		if self.tagEditor.text() != '' and self.tagEditor.text() != ' ':
			newButton = QtGui.QPushButton(self.tagEditor.text(),self)
			newButton.setStyleSheet("Text-align:mid")
			#newButton.setAlignment(QtCore.Qt.AlignLeft)
			if (10*len(self.tagEditor.text())) < 70:
				newButton.setFixedWidth(70)
			else:
				newButton.setFixedWidth(10*len(self.tagEditor.text()))
			self.tagLayout.addWidget(newButton)
			self.tempWigdets.append(newButton)
			# print self.tempWigdets

			# update the layout
			self.setLayout(self.mainLayout)
			# append the defined label to our label set
			self.labelSet.append(str(self.tagEditor.text()))
			self.labelSet = list(set(self.labelSet))
			# clear the editor after getting the text
			# update the string list
			self.tagEditorModel.setStringList(self.labelSet)
			self.tagEditor.clear()

	def removeAllLabels(self):
		'''
		remove all labels created in tagLayout(which are stored in self.tempWidgets)
		'''
		# print 'remove widgets'
		for item in self.tempWigdets:
			self.tagLayout.removeWidget(item)
			item.deleteLater()
			item = None
		# update the layout to refresh UI and clear the tempWidget for next image labels
		self.tempWigdets = list()
		self.setLayout(self.mainLayout)

	def saveLabels(self):
		'''
		save all the unique labels for current image to result file
		'''
		# save all labels in self.tempWigdets and dump them to result.jl
		if self.inputFilePath != '' and self.outputFile != '':
			curImgLabels = list()
			for widget in self.tempWigdets:
				curImgLabels.append(str(widget.text()))

			
			flag = False
			temp = []
			with open(self.outputFile, 'ab+') as f: # in this mode the file can add new text
				for line in f.readlines():
					item = json.loads(line)
					# if already labeled, update it
					if item['index'] == self.curImgIndex:
						item['labels'] = curImgLabels
						flag = True
					# store the whole updated text for copying into new file
					temp.append(item)

				if flag == False: # still unlabeled
					if self.curImgIndex > len(temp)+1:
						# print self.curImgIndex,str(len(temp)+1)
						# if skipped
						QtGui.QMessageBox.information(self, "Mistake", "You must have skipped some images,"\
							"double check that! \n Your current position should be " + str(len(temp)+1) + \
							", not "+ str(self.curImgIndex))
					else:
						new_item=dict(index=self.curImgIndex,labels=curImgLabels)
						f.write(json.dumps(new_item) + "\n")
			if flag == True: #labelled, update the whole file
				with open(self.outputFile,'w') as f: # in this mode the file will be erased first and written in new text
					for line in temp:
						f.write(json.dumps(line) + "\n")

		else:
			QtGui.QMessageBox.information(self, "Warning", "Make sure you have selected input and output files")
		# refresh
		self.removeAllLabels()

	def discardImg(self):
		pass



	def setEditorWidth(self):
		if (10*len(self.tagEditor.text())) < 70:
			self.tagEditor.setFixedWidth(70)
		else:
			self.tagEditor.setFixedWidth(10*len(self.tagEditor.text()))

	# event handlers
	def inputFileDialog(self):
		# the file directory for input images
		self.inputFilePath = str(QtGui.QFileDialog.getExistingDirectory(self, 'input file directory', '/home'))
		if self.inputFilePath != '':
			self.MaxImgIndex = len([file for file in listdir(self.inputFilePath) if isfile(join(self.inputFilePath,file))])
			self.inputFileLabel.setText('Input File: ' + self.inputFilePath)
			# print self.MaxImgIndex
		else:
			QtGui.QMessageBox.information(self, "Message", "You should select a file directory to continue")

	def outputFileDialog(self):
		# the file for output label text
		self.outputFile = str(QtGui.QFileDialog.getOpenFileName(self, 'output file','/home'))
		if self.outputFile != '':
			# there is already an output file
			with open(self.outputFile,'rb+') as f:
				content = f.readlines()
				self.curImgIndex = len(content) # if result file is empty then the index is 0
				self.updateStatusBar()
				self.showNextImg() # show the first(next of last commitment) image and increase current index by 1

				# load label set
			
				for line in content:
					item = json.loads(line)
					labels = item['labels']
					self.labelSet.extend(labels)
				self.labelSet = list(set(self.labelSet))
				# print self.labelSet
				# update the string list
				self.tagEditorModel.setStringList(self.labelSet)

			self.outputFileLabel.setText('Output File: ' + self.outputFile)
		else:
			QtGui.QMessageBox.information(self, "Message", "You should select an output file to continue")

		

	def showImg(self,path):
		pixmap = QtGui.QPixmap(path)
		self.imgLabel.setPixmap(pixmap)
		# self.removeAllLabels()

	def showPrevImg(self):
		if self.inputFilePath != '' and self.outputFile != '':
			if self.curImgIndex > 1:
				self.curImgIndex -= 1
				self.updateStatusBar()
				# preImgPath = join(self.inputFilePath,str(self.curImgIndex)+'.jpg')
				preImgPath = join(self.inputFilePath,str(self.curImgIndex)+'.png')
				if not isfile(preImgPath):
					preImgPath = join(self.inputFilePath,str(self.curImgIndex)+'.jpg')
				self.showImg(preImgPath)
			else:
				QtGui.QMessageBox.information(self, "Warning", "There is no previous image")
		else:
			QtGui.QMessageBox.information(self, "Warning", "You should select an input file to show images and " \
				"output file to store result")

	def showNextImg(self):
		if self.inputFilePath != '' and self.outputFile != '':
			if self.curImgIndex < self.MaxImgIndex:
				self.curImgIndex += 1
				self.updateStatusBar()
				# both jpg and png format can be displayed
				nextImgPath = join(self.inputFilePath,str(self.curImgIndex)+'.png')
				if not isfile(nextImgPath):
					nextImgPath = join(self.inputFilePath,str(self.curImgIndex)+'.jpg')
				self.showImg(nextImgPath)
			else:
				QtGui.QMessageBox.information(self, "Warning", "There is no next image")
		else:
			QtGui.QMessageBox.information(self, "Warning", "You should select an input file to show images and " \
				"output file to store result")


	def updateStatusBar(self):
		self.progressBar.showMessage('current progress: ' + str(self.curImgIndex) + '/' + str(self.MaxImgIndex))


class MyMainWindow(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(MyMainWindow, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.initWindow()
		


	def initWindow(self):
		self.widget = MyWidget()
		self.setCentralWidget(self.widget)

		QtGui.QShortcut(QtGui.QKeySequence("Alt+q"), self, self.close)

		icon_path = join(getcwd(),'icon.png')
		self.setWindowIcon(QtGui.QIcon(icon_path))
		self.setGeometry(300, 300, 700, 500)
		self.setWindowTitle('imgLab')
		self.center()
		self.show() 


	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(self, 'Message',
			"Are you sure to quit?", QtGui.QMessageBox.Yes | 
				QtGui.QMessageBox.No, QtGui.QMessageBox.No)

		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

def main():
	app = QtGui.QApplication(sys.argv)
	foo = MyMainWindow()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()



