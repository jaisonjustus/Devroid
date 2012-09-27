from PyQt4 import QtGui,QtCore
from drawable.MainWindow import *
from modules.CreateNewProjectUI import *
import sys

class DevroidApp(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.mainWindow = Ui_MainWindow()
		self.mainWindow.setupUi(self)
		self.eventBindings()

	def eventBindings(self):
		QtCore.QObject.connect(self.mainWindow.actionNewProject, QtCore.SIGNAL('triggered()'), self.createProject)

	def createProject(self):
		self.createForm = CreateNewProjectUI(self.mainWindow.MainFormFrame)
		self.mainWindow.mainFormFrameLayout.addWidget(self.createForm.getFormWrapperFrame())
		#self.mainWindow.mainFormFrameLayout.setGeometry(QtCore.QRect(0,0,100,100))
		#self.mainWindow.MainFormFrame.setStyleSheet("QPushButton { background-color:none; }");

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	appMainWindow = DevroidApp()
	appMainWindow.show()
	app.exec_()