#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

# class Example(QtGui.QWidget):
    
#     def __init__(self):
#         super(Example, self).__init__()
        
#         self.initUI()
        
#     def initUI(self):      

#         cb = QtGui.QCheckBox('Show title', self)
#         cb.move(20, 20)
#         cb.toggle()
#         cb.stateChanged.connect(self.changeTitle)
        
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('QtGui.QCheckBox')
#         self.show()
        
#     def changeTitle(self, state):
      
#         if state == QtCore.Qt.Checked:
#             self.setWindowTitle('QtGui.QCheckBox')
#         else:
#             self.setWindowTitle('')

# # toggle button
# class Example(QtGui.QWidget):
    
#     def __init__(self):
#         super(Example, self).__init__()
        
#         self.initUI()
        
        
#     def initUI(self):      

#         self.col = QtGui.QColor(0, 0, 0)       

#         redb = QtGui.QPushButton('Red', self)
#         redb.setCheckable(True)
#         redb.move(10, 10)

#         redb.clicked.connect(self.setColor)

#         greenb = QtGui.QPushButton('Green', self)
#         greenb.setCheckable(True)
#         greenb.move(10, 60)

#         greenb.clicked.connect(self.setColor)

#         blueb = QtGui.QPushButton('Blue', self)
#         blueb.setCheckable(True)
#         blueb.move(10, 110)

#         blueb.clicked.connect(self.setColor)

#         self.square = QtGui.QFrame(self)
#         self.square.setGeometry(150, 20, 10, 10)
#         self.square.setStyleSheet("QWidget { background-color: %s }" %  
#             self.col.name())

#         self.label = QtGui.QLabel(self)
#         self.label.setPixmap(QtGui.QPixmap('icon.png'))
#         self.label.setGeometry(160, 40,100,100)
#         self.label.setScaledContents(True)
        
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('Toggle button')
#         self.show()
        
        
#     def setColor(self, pressed):
        
#         source = self.sender()
#         self.col = QtGui.QColor(0, 0, 0)

#         if pressed:
#             val = 255
#         else: val = 0
                        
#         if source.text() == "Red":
#             self.col.setRed(val)                
#         elif source.text() == "Green":
#             self.col.setGreen(val)             
#         else:
#             self.col.setBlue(val) 
            
#         self.square.setStyleSheet("QFrame { background-color: %s }" %
#             self.col.name())  

# pixmap widget
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("icon.png")

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        #hbox.addStretch(1)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()

# # QLineEdit
# class Example(QtGui.QWidget):
    
#     def __init__(self):
#         super(Example, self).__init__()
        
#         self.initUI()
        
#     def initUI(self):      

#         self.lbl = QtGui.QLabel(self)
#         qle = QtGui.QLineEdit(self)
        
#         qle.move(60, 100)
#         self.lbl.move(60, 40)

#         qle.textChanged[str].connect(self.onChanged)
        
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle('QtGui.QLineEdit')
#         self.show()
        
#     def onChanged(self, text):
        
#         self.lbl.setText(text)
#         self.lbl.adjustSize()  
  

# # splitters
# class Example(QtGui.QWidget):
    
#     def __init__(self):
#         super(Example, self).__init__()
        
#         self.initUI()
        
#     def initUI(self):      

#         vbox = QtGui.QVBoxLayout(self)

#         topleft = QtGui.QFrame(self)
#         topleft.setFrameShape(QtGui.QFrame.StyledPanel)
 
#         topright = QtGui.QFrame(self)
#         topright.setFrameShape(QtGui.QFrame.StyledPanel)

#         bottom = QtGui.QFrame(self)
#         bottom.setFrameShape(QtGui.QFrame.StyledPanel)

#         lbl = QtGui.QLabel('label',self)

#         splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
#         splitter1.addWidget(topleft)
#         splitter1.addWidget(topright)

#         # splitter 2 contains splitter1 and another widget
#         splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
#         splitter2.addWidget(splitter1)
#         splitter2.addWidget(bottom)
#         # splitter2.addWidget(lbl)

#         vbox.addWidget(splitter2)
#         vbox.addWidget(lbl)
#         self.setLayout(vbox)
#         QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QtGui.QSplitter')
#         self.show()

# # QComboBox
# class Example(QtGui.QWidget):
    
#     def __init__(self):
#         super(Example, self).__init__()
        
#         self.initUI()
        
#     def initUI(self):      

#         self.lbl = QtGui.QLabel("Ubuntu", self)

#         combo = QtGui.QComboBox(self)
#         combo.addItem("Ubuntu")
#         combo.addItem("Mandriva")
#         combo.addItem("Fedora")
#         combo.addItem("Red Hat")
#         combo.addItem("Gentoo")

#         combo.move(50, 50)
#         self.lbl.move(50, 150)

#         combo.activated[str].connect(self.onActivated)        
         
#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('QtGui.QComboBox')
#         self.show()
        
#     def onActivated(self, text):
      
#         self.lbl.setText(text)
#         self.lbl.adjustSize() 

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()