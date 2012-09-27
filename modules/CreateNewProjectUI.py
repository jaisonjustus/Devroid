from PyQt4 import QtGui,QtCore
from drawable.CreateNewProjectForm import *
import sys

class CreateNewProjectUI:
	def __init__(self,parent):
		self.form = Ui_Form()
		self.form.setupUi(parent)
		self.loadEventBindings()

	def loadEventBindings(self):
		QtCore.QObject.connect(self.form.pushButton, QtCore.SIGNAL('pressed()'), self.printText)

	def getFormWrapperFrame(self):
		return self.form.frame

	def printText(self):
		print "Button pressed...."