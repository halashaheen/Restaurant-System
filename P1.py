# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from TR import Table_Rerservation
from add import Cashier
from feedback_gui import Feedback
from testing.waiter_gui import  Waiter_information
from PyQt5 import QtCore, QtGui, QtWidgets


class Main_menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Shonar Bangla")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(300, 300))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("fast-food-6e63ccd9d1bf563d07b0e4afe80b8f88.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 70))
        font = QtGui.QFont()
        font.setFamily("Shonar Bangla")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Shonar Bangla")
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 70))
        font = QtGui.QFont()
        font.setFamily("Shonar Bangla")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 70))
        font = QtGui.QFont()
        font.setFamily("Shonar Bangla")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.pushButton_4.clicked.connect(lambda :self.cashier_view())
        self.pushButton.clicked.connect(lambda :self.table_reservation_page_view())
        self.pushButton_3.clicked.connect(lambda :self.feedback_view())
        self.pushButton_2.clicked.connect(lambda :self.waiter_view())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dinner Club"))
        self.label.setText(_translate("MainWindow", " Welcome to Dinner Club"))
        self.pushButton.setText(_translate("MainWindow", "Tables\'  Reservation"))
        self.pushButton_2.setText(_translate("MainWindow", "Waiters\' Information"))
        self.pushButton_4.setText(_translate("MainWindow", "Cashier"))
        self.pushButton_3.setText(_translate("MainWindow", "Feedback"))

    def waiter_view(self):
        waiter_ui = Waiter_information()
        waiter_ui.setupUi(MainWindow)
        waiter_ui.pushButton_3.clicked.connect(lambda :self.setupUi(MainWindow))


    def table_reservation_page_view(self):
        table_ui = Table_Rerservation()
        table_ui.setupUi(MainWindow)
        table_ui.pushButton_10.clicked.connect(lambda :self.setupUi(MainWindow))

    def cashier_view(self):
        cashier_ui = Cashier()
        cashier_ui.setupUi(MainWindow)
        cashier_ui.pushButton_4.clicked.connect(lambda :self.setupUi(MainWindow))

    def feedback_view(self):
        feedback_ui = Feedback()
        feedback_ui.setupUi(MainWindow)
        feedback_ui.pushButton_2.clicked.connect(lambda: self.setupUi(MainWindow))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_ui = Main_menu()
    main_ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())