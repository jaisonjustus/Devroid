# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateNewProjectForm.ui'
#
# Created: Fri Sep 28 15:54:36 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(396, 326)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.create_project_form = QtGui.QFrame(Form)
        self.create_project_form.setGeometry(QtCore.QRect(-10, 0, 441, 511))
        self.create_project_form.setStyleSheet(_fromUtf8("background-color:rgb(38,38,38);\n"
"border-color:rgb(38,38,38);"))
        self.create_project_form.setFrameShape(QtGui.QFrame.StyledPanel)
        self.create_project_form.setFrameShadow(QtGui.QFrame.Raised)
        self.create_project_form.setObjectName(_fromUtf8("create_project_form"))
        self.gridLayoutWidget = QtGui.QWidget(self.create_project_form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 361, 221))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 11pt \"Roboto\";\n"
"color:white;"))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Project Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet(_fromUtf8("font: 75 11pt \"Roboto\";\n"
"color:white;"))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Andriod Version", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet(_fromUtf8("font: 75 11pt \"Roboto\";\n"
"color:white;"))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Project Path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet(_fromUtf8("font: 75 11pt \"Roboto\";\n"
"color:white;"))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Activity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet(_fromUtf8("font: 75 11pt \"Roboto\";\n"
"color:white;"))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Package", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.project_name_text = QtGui.QTextEdit(self.gridLayoutWidget)
        self.project_name_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.project_name_text.setStyleSheet(_fromUtf8("background-color:none;"))
        self.project_name_text.setTabChangesFocus(True)
        self.project_name_text.setObjectName(_fromUtf8("project_name_text"))
        self.gridLayout.addWidget(self.project_name_text, 0, 1, 1, 1)
        self.project_path_text = QtGui.QTextEdit(self.gridLayoutWidget)
        self.project_path_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.project_path_text.setStyleSheet(_fromUtf8("background-color:none;"))
        self.project_path_text.setTabChangesFocus(True)
        self.project_path_text.setObjectName(_fromUtf8("project_path_text"))
        self.gridLayout.addWidget(self.project_path_text, 2, 1, 1, 1)
        self.activity_text = QtGui.QTextEdit(self.gridLayoutWidget)
        self.activity_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.activity_text.setStyleSheet(_fromUtf8("background-color:none;"))
        self.activity_text.setTabChangesFocus(True)
        self.activity_text.setObjectName(_fromUtf8("activity_text"))
        self.gridLayout.addWidget(self.activity_text, 3, 1, 1, 1)
        self.package_text = QtGui.QTextEdit(self.gridLayoutWidget)
        self.package_text.setMaximumSize(QtCore.QSize(16777215, 30))
        self.package_text.setStyleSheet(_fromUtf8("background-color:none;"))
        self.package_text.setTabChangesFocus(True)
        self.package_text.setObjectName(_fromUtf8("package_text"))
        self.gridLayout.addWidget(self.package_text, 4, 1, 1, 1)
        self.android_version_combo = QtGui.QComboBox(self.gridLayoutWidget)
        self.android_version_combo.setMinimumSize(QtCore.QSize(0, 30))
        self.android_version_combo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.android_version_combo.setStyleSheet(_fromUtf8("QComboBox{\n"
"    background-color:none;\n"
"}"))
        self.android_version_combo.setObjectName(_fromUtf8("android_version_combo"))
        self.gridLayout.addWidget(self.android_version_combo, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.create_project_form)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Roboto\";\n"
"color:white;"))
        self.label.setText(QtGui.QApplication.translate("Form", "Create New Andriod Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.create_project_form)
        self.line.setGeometry(QtCore.QRect(0, 40, 521, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.create_android_project_button = QtGui.QPushButton(self.create_project_form)
        self.create_android_project_button.setGeometry(QtCore.QRect(250, 290, 131, 27))
        self.create_android_project_button.setStyleSheet(_fromUtf8("QPushButton     {\n"
"    background-color:none;\n"
"}"))
        self.create_android_project_button.setText(QtGui.QApplication.translate("Form", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.create_android_project_button.setObjectName(_fromUtf8("create_android_project_button"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

