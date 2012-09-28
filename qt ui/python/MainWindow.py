# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Fri Sep 28 16:00:18 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(803, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Android Development ToolKit", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/android_logo_big.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -30, 821, 611))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(48, 48, 48);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(50, 20, 271, 331))
        self.frame_2.setStyleSheet(_fromUtf8("image: url(:/images/android_logo_big.png);\n"
"border :0;"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 310, 111, 41))
        self.label.setStyleSheet(_fromUtf8("font: 63 10pt \"Open Sans\";\n"
"color:white"))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Development ToolKit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 300, 141, 61))
        self.label_3.setStyleSheet(_fromUtf8("font: 75 bold 24pt \"Open Sans\";\n"
"color:white"))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Android", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayoutWidget = QtGui.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 460, 271, 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet(_fromUtf8("font: 25 9pt \"Open Sans\";\n"
"color: white;"))
        self.label_4.setLineWidth(0)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "version : 0.0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet(_fromUtf8("font: 25 9pt \"Open Sans\";\n"
"color: white;"))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "license : GPL License", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet(_fromUtf8("font: 25 9pt \"Open Sans\";\n"
"color: white;"))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "source : github/jaisonjustus/devroid", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(70, 360, 261, 71))
        self.label_7.setStyleSheet(_fromUtf8("color:white;\n"
"font: 25 11pt \"Open Sans\";"))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Android development toolkit to create android projects and manage project binaries between emulators and devices. ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.MainFormFrame = QtGui.QFrame(self.frame)
        self.MainFormFrame.setGeometry(QtCore.QRect(360, 70, 431, 501))
        self.MainFormFrame.setAutoFillBackground(False)
        self.MainFormFrame.setStyleSheet(_fromUtf8("border:0;"))
        self.MainFormFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.MainFormFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.MainFormFrame.setObjectName(_fromUtf8("MainFormFrame"))
        self.verticalLayoutWidget = QtGui.QWidget(self.MainFormFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 160, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.main_form_frame_layout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.main_form_frame_layout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.main_form_frame_layout.setMargin(0)
        self.main_form_frame_layout.setObjectName(_fromUtf8("main_form_frame_layout"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Android", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNewProject = QtGui.QAction(MainWindow)
        self.actionNewProject.setText(QtGui.QApplication.translate("MainWindow", "New Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewProject.setObjectName(_fromUtf8("actionNewProject"))
        self.actionBuild_Project = QtGui.QAction(MainWindow)
        self.actionBuild_Project.setText(QtGui.QApplication.translate("MainWindow", "Build Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionBuild_Project.setObjectName(_fromUtf8("actionBuild_Project"))
        self.actionInstall_Project = QtGui.QAction(MainWindow)
        self.actionInstall_Project.setText(QtGui.QApplication.translate("MainWindow", "Install Project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInstall_Project.setObjectName(_fromUtf8("actionInstall_Project"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionProjects = QtGui.QAction(MainWindow)
        self.actionProjects.setText(QtGui.QApplication.translate("MainWindow", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProjects.setObjectName(_fromUtf8("actionProjects"))
        self.action_android_paths = QtGui.QAction(MainWindow)
        self.action_android_paths.setText(QtGui.QApplication.translate("MainWindow", "Android Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.action_android_paths.setObjectName(_fromUtf8("action_android_paths"))
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionNewProject)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionBuild_Project)
        self.menuTools.addAction(self.actionInstall_Project)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionExit)
        self.menuSettings.addAction(self.actionProjects)
        self.menuSettings.addAction(self.action_android_paths)
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

import deveroid_rc
