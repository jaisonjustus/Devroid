from PyQt4 import QtGui,QtCore
from drawable.CreateNewProjectForm import *
import sys

class CreateNewProjectUI:
	def __init__(self, settings, parent):
		# saving application settings
		self.settings = settings

		# initializing the create android project form
		self.form = Ui_Form()
		self.form.setupUi(parent)
		
		# preparing data and event bindings for the form
		self.populating_default_form_data()
		self.load_event_bindings()

	# loading the event bindings for the form
	def load_event_bindings(self):
		QtCore.QObject.connect(self.form.create_android_project_button, QtCore.SIGNAL('pressed()'), self.get_project_details)

	def getFormWrapperFrame(self):
		return self.form.create_project_form

	def get_project_details(self):
		project_name = self.form.project_name_text.toPlainText()
		android_version = str(self.form.android_version_combo.currentText())
		project_path = self.form.project_path_text.toPlainText()
		activity = self.form.activity_text.toPlainText()
		package = self.form.package_text.toPlainText()

		print "android create project --target " + self.settings.android_target_versions[android_version] + " --name " + project_name + " path " + project_path + " --activity " + activity + " --package " + package

	def populating_default_form_data(self):
		self.form.android_version_combo.addItems(self.settings.android_target_versions.keys())
