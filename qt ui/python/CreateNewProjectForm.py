# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateNewProjectForm.ui'
#
# Created: Thu Sep 27 16:33:02 2012
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
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 431, 511))
        self.frame.setStyleSheet(_fromUtf8("background-color:rgb(38,38,38);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame)
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
        self.textEdit = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:none;"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        self.textEdit_2 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_2.setStyleSheet(_fromUtf8("background-color:none;"))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.textEdit_3 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_3.setStyleSheet(_fromUtf8("background-color:none;"))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.gridLayout.addWidget(self.textEdit_3, 2, 1, 1, 1)
        self.textEdit_4 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_4.setStyleSheet(_fromUtf8("background-color:none;"))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.gridLayout.addWidget(self.textEdit_4, 3, 1, 1, 1)
        self.textEdit_5 = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_5.setStyleSheet(_fromUtf8("background-color:none;"))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.gridLayout.addWidget(self.textEdit_5, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 321, 31))
        self.label.setStyleSheet(_fromUtf8("font: 75 16pt \"Roboto\";\n"
"color:white;"))
        self.label.setText(QtGui.QApplication.translate("Form", "Create New Andriod Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 40, 521, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(250, 290, 131, 27))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton    {\n"
"background-color:none;\n"
"}\n"
"\n"
"QPushButton :hover    {\n"
"background-color:rgb(255,255,255);\n"
"}"))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

