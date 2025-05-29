# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainjhVtdA.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_R = QLabel(self.centralwidget)
        self.label_R.setObjectName(u"label_R")
        self.label_R.setMinimumSize(QSize(0, 0))
        self.label_R.setStyleSheet(u"font-size:10pt;")

        self.horizontalLayout.addWidget(self.label_R)

        self.label_S = QLabel(self.centralwidget)
        self.label_S.setObjectName(u"label_S")
        self.label_S.setStyleSheet(u"font-size:10pt;")

        self.horizontalLayout.addWidget(self.label_S)

        self.label_T = QLabel(self.centralwidget)
        self.label_T.setObjectName(u"label_T")
        self.label_T.setStyleSheet(u"\n"
"font-size:10pt;")

        self.horizontalLayout.addWidget(self.label_T)

        self.label_Kondisi = QLabel(self.centralwidget)
        self.label_Kondisi.setObjectName(u"label_Kondisi")
        self.label_Kondisi.setStyleSheet(u"font-size:10pt;")

        self.horizontalLayout.addWidget(self.label_Kondisi)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.line_R = QLineEdit(self.centralwidget)
        self.line_R.setObjectName(u"line_R")
        self.line_R.setBaseSize(QSize(30, 30))
        self.line_R.setStyleSheet(u"font-size:20pt;")

        self.horizontalLayout_3.addWidget(self.line_R)

        self.line_S = QLineEdit(self.centralwidget)
        self.line_S.setObjectName(u"line_S")
        self.line_S.setStyleSheet(u"font-size:20pt;")

        self.horizontalLayout_3.addWidget(self.line_S)

        self.line_T = QLineEdit(self.centralwidget)
        self.line_T.setObjectName(u"line_T")
        self.line_T.setStyleSheet(u"font-size:20pt;")

        self.horizontalLayout_3.addWidget(self.line_T)

        self.line_Status = QLineEdit(self.centralwidget)
        self.line_Status.setObjectName(u"line_Status")
        self.line_Status.setStyleSheet(u"font-size:20pt;")

        self.horizontalLayout_3.addWidget(self.line_Status)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 7, -1, -1)
        self.Button_Start = QPushButton(self.centralwidget)
        self.Button_Start.setObjectName(u"Button_Start")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Start.sizePolicy().hasHeightForWidth())
        self.Button_Start.setSizePolicy(sizePolicy)
        self.Button_Start.setMinimumSize(QSize(0, 0))
        self.Button_Start.setBaseSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.Button_Start)

        self.Box_port = QComboBox(self.centralwidget)
        self.Box_port.setObjectName(u"Box_port")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Box_port.sizePolicy().hasHeightForWidth())
        self.Box_port.setSizePolicy(sizePolicy1)
        self.Box_port.setBaseSize(QSize(20, 0))

        self.horizontalLayout_6.addWidget(self.Box_port)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_R.setText(QCoreApplication.translate("MainWindow", u"Tegangan R", None))
        self.label_S.setText(QCoreApplication.translate("MainWindow", u"Tegangan S", None))
        self.label_T.setText(QCoreApplication.translate("MainWindow", u"Tegangan T", None))
        self.label_Kondisi.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.line_R.setText("")
        self.Button_Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.Box_port.setCurrentText("")
        self.Box_port.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Port...", None))
    # retranslateUi

