from PyQt4 import QtGui,QtCore
from drawable.MainWindow import *
from modules.CreateNewProjectUI import *
from modules.Settings import *
import sys

class DevroidApp(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.mainWindow = Ui_MainWindow()
		self.mainWindow.setupUi(self)
		self.event_bindings()
		self.settings = Settings()

	def event_bindings(self):
		print "event bindings"
		QtCore.QObject.connect(self.mainWindow.actionNewProject, QtCore.SIGNAL('triggered()'), self.create_new_project)

	def create_new_project(self):
		self.create_app_form = CreateNewProjectUI(self.settings, self.mainWindow.MainFormFrame)
		self.mainWindow.main_form_frame_layout.addWidget(self.create_app_form.get_form_wrapper_frame())
		#self.mainWindow.main_form_frame_layout.setGeometry(QtCore.QRect(0,0,100,100))
		#self.mainWindow.MainFormFrame.setStyleSheet("QPushButton { background-color:none; }");

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	appMainWindow = DevroidApp()
	appMainWindow.show()
	app.exec_()