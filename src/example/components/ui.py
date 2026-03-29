# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 260)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setGeometry(QRect(20, 20, 60, 20))
        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(90, 20, 400, 24))
        self.button_true = QPushButton(self.centralwidget)
        self.button_true.setObjectName(u"button_true")
        self.button_true.setGeometry(QRect(20, 60, 60, 28))
        self.button_false = QPushButton(self.centralwidget)
        self.button_false.setObjectName(u"button_false")
        self.button_false.setGeometry(QRect(90, 60, 60, 28))
        self.button_and = QPushButton(self.centralwidget)
        self.button_and.setObjectName(u"button_and")
        self.button_and.setGeometry(QRect(160, 60, 70, 28))
        self.button_or = QPushButton(self.centralwidget)
        self.button_or.setObjectName(u"button_or")
        self.button_or.setGeometry(QRect(240, 60, 60, 28))
        self.button_not = QPushButton(self.centralwidget)
        self.button_not.setObjectName(u"button_not")
        self.button_not.setGeometry(QRect(310, 60, 70, 28))
        self.button_lparen = QPushButton(self.centralwidget)
        self.button_lparen.setObjectName(u"button_lparen")
        self.button_lparen.setGeometry(QRect(390, 60, 45, 28))
        self.button_rparen = QPushButton(self.centralwidget)
        self.button_rparen.setObjectName(u"button_rparen")
        self.button_rparen.setGeometry(QRect(445, 60, 45, 28))
        self.button_equal = QPushButton(self.centralwidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setGeometry(QRect(20, 100, 470, 30))
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(20, 150, 60, 20))
        self.result_text = QLineEdit(self.centralwidget)
        self.result_text.setObjectName(u"result_text")
        self.result_text.setGeometry(QRect(90, 150, 120, 24))
        self.result_text.setReadOnly(True)
        self.prefix_label = QLabel(self.centralwidget)
        self.prefix_label.setObjectName(u"prefix_label")
        self.prefix_label.setGeometry(QRect(20, 190, 60, 20))
        self.prefix_text = QLineEdit(self.centralwidget)
        self.prefix_text.setObjectName(u"prefix_text")
        self.prefix_text.setGeometry(QRect(90, 190, 400, 24))
        self.prefix_text.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Propositional Logic Evaluator", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.button_true.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.button_false.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.button_and.setText(QCoreApplication.translate("MainWindow", u"AND", None))
        self.button_or.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.button_not.setText(QCoreApplication.translate("MainWindow", u"NOT", None))
        self.button_lparen.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.button_rparen.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.prefix_label.setText(QCoreApplication.translate("MainWindow", u"Prefix:", None))
