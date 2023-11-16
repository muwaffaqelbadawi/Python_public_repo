from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    
    self.title = 'PyQt5 Layout Management'
    self.left = 400
    self.top = 200
    self.width = 400
    self.height = 100
    self.iconName = '../snakeHead.png'
    
    self.setWindowTitle(title)
    self.setWindowIcon(QtGui.QIcon(iconName))
    self.setGeometry(left, top, width, height)
    
    self.CreateButton()
    
    
    
    def InitWindow(self):
      self.setWindowTitle(self.title)
      self.setWindowIcon(self.nameIcon)
      self.setGeometr(self.left,self.top,self.right,self.hieght())
      self.setWindowTitle()
    
    self.show()
    
  def CreateButton(self):
    button = QPushButton('Close Application', self)
    # button.move(50,50)
    button.setGeometry(QRect(100,100,140,30))
    button.setIcon(QtGui.QIcon('../snakeHead.png'))
    button.setIconSize(QtCore.QSize(40,40))
    button.clicked.connect(self.clickMe)
    # button.setToolTip('<h2>This is click me button</h2>')
    
  def clickMe(self):
    raise SystemExit

if __name__ == '__main__':
  App = QApplication(sys.argv)
  window = Window()
  sys.exit(App.exec())