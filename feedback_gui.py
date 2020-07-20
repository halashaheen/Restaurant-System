# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedback_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Feedback(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.feedback = QtWidgets.QWidget()
        self.feedback.setObjectName("feedback")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.feedback)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FeedBack = QtWidgets.QGroupBox(self.feedback)
        self.FeedBack.setMaximumSize(QtCore.QSize(441, 311))
        self.FeedBack.setObjectName("FeedBack")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FeedBack)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.FeedBack)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.FeedBack)
        self.tabWidget.addTab(self.feedback, "")
        self.totalreview = QtWidgets.QWidget()
        self.totalreview.setObjectName("totalreview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.totalreview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.totalreview)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.totalreview)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_5.addWidget(self.toolButton)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_5.addWidget(self.toolButton_2)
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout_5.addWidget(self.toolButton_3)
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_4.setObjectName("toolButton_4")
        self.verticalLayout_5.addWidget(self.toolButton_4)
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_5.setObjectName("toolButton_5")
        self.verticalLayout_5.addWidget(self.toolButton_5)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_4.addWidget(self.progressBar_2)
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout_4.addWidget(self.progressBar_3)
        self.progressBar_4 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout_4.addWidget(self.progressBar_4)
        self.progressBar_5 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout_4.addWidget(self.progressBar_5)
        self.progressBar_6 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName("progressBar_6")
        self.verticalLayout_4.addWidget(self.progressBar_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.totalreview, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 21))
        self.menubar.setObjectName("menubar")
        self.menufeedback = QtWidgets.QMenu(self.menubar)
        self.menufeedback.setObjectName("menufeedback")
        self.menusubmit = QtWidgets.QMenu(self.menubar)
        self.menusubmit.setObjectName("menusubmit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontakefb = QtWidgets.QAction(MainWindow)
        self.actiontakefb.setObjectName("actiontakefb")
        self.actiontotal = QtWidgets.QAction(MainWindow)
        self.actiontotal.setObjectName("actiontotal")
        self.menufeedback.addAction(self.actiontakefb)
        self.menusubmit.addAction(self.actiontotal)
        self.menubar.addAction(self.menufeedback.menuAction())
        self.menubar.addAction(self.menusubmit.menuAction())
        self.actiontakefb.triggered.connect(lambda :self.Save_button_function())
        self.actiontotal.triggered.connect(lambda :self.Average_button_function())
        self.pushButton.clicked.connect(MainWindow.close)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Feedback"))
        self.FeedBack.setTitle(_translate("MainWindow", "Customer Feedback"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.feedback), _translate("MainWindow", "Tab 1"))
        self.groupBox.setTitle(_translate("MainWindow", "Average Customer Review"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Customers feedback"))
        self.toolButton.setText(_translate("MainWindow", "5"))
        self.toolButton_2.setText(_translate("MainWindow", "4"))
        self.toolButton_3.setText(_translate("MainWindow", "3"))
        self.toolButton_4.setText(_translate("MainWindow", "2"))
        self.toolButton_5.setText(_translate("MainWindow", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.totalreview), _translate("MainWindow", "Tab 2"))
        self.pushButton_2.setText(_translate("MainWindow", "Back to Main Menu"))
        self.pushButton.setText(_translate("MainWindow", "close"))
        self.menufeedback.setTitle(_translate("MainWindow", "run"))
        self.menusubmit.setTitle(_translate("MainWindow", "submit"))
        self.actiontakefb.setText(_translate("MainWindow", "save"))
        self.actiontotal.setText(_translate("MainWindow", "Average"))
        self.tabWidget.setCurrentWidget(self.feedback)

    def submit(self,in_file):

        f1 = open(in_file, 'r')
        list = []

        for line in f1:
            list.append(int(line.strip('\n')))
            count5 = list.count(5)
            count4 = list.count(4)
            count3 = list.count(3)
            count2 = list.count(2)
            count1 = list.count(1)
        num = count1 + count2 + count3 + count4 + count5
        avg = 20 * (count1 + count2 * 2 + count3 * 3 + count4 * 4 + count5 * 5) / num
        return avg

    def c3(self,input_file3):
        f3 = open(input_file3, 'r')
        list = []
        for line in f3:
            list.append(int(line.strip('\n')))
            count5 = list.count(5)
            count4 = list.count(4)
            count3 = list.count(3)
            count2 = list.count(2)
            count1 = list.count(1)
        num = count1 + count2 + count3 + count4 + count5
        avg3 = 20 * (count3 * 3) / num
        return avg3

    def c4(self,input_file4):
        f4 = open(input_file4, 'r')
        list = []
        for line in f4:
            list.append(int(line.strip('\n')))
            count5 = list.count(5)
            count4 = list.count(4)
            count3 = list.count(3)
            count2 = list.count(2)
            count1 = list.count(1)
        num = count1 + count2 + count3 + count4 + count5
        avg4 = 20 * (count4 * 4) / num
        return avg4

    def c5(self,input_file5):
        f5 = open(input_file5, 'r')
        list = []
        for line in f5:
            list.append(int(line.strip('\n')))
            count5 = list.count(5)
            count4 = list.count(4)
            count3 = list.count(3)
            count2 = list.count(2)
            count1 = list.count(1)
        num = count1 + count2 + count3 + count4 + count5
        avg5 = 20 * (count5 * 5) / num
        return avg5

    def c2(self,input_file2):
        f2 = open(input_file2, 'r')
        list = []
        for line in f2:
            list.append(int(line.strip('\n')))
            count5 = list.count(5)
            count4 = list.count(4)
            count3 = list.count(3)
            count2 = list.count(2)
            count1 = list.count(1)
        num = count1 + count2 + count3 + count4 + count5
        avg2 = 20 * (count2 * 2) / num
        return avg2

    def c1(self,input_file1):
        f1 = open(input_file1, 'r')
        list = []
        for line in f1:
            list.append(int(line.strip('\n')))
            count5 = list.count(5)
            count4 = list.count(4)
            count3 = list.count(3)
            count2 = list.count(2)
            count1 = list.count(1)
        num = count1 + count2 + count3 + count4 + count5
        avg1 = 20 * (count1 * 1) / num
        return avg1

    def c1(self,input_file1):
        f1 = open(input_file1, 'r')
        list = []
        for line in f1:
            list.append(int(line.strip('\n')))
            count5 = list.count(5)
            count4 = list.count(4)
            count3 = list.count(3)
            count2 = list.count(2)
            count1 = list.count(1)
        num = count1 + count2 + count3 + count4 + count5
        avg1 = 20 * (count1 * 1) / num
        return avg1

    def Average_button_function(self):
        self.progressBar.setProperty("value", self.submit("Feedback.txt"))
        self.progressBar_2.setProperty("value", self.c5("Feedback.txt"))
        self.progressBar_3.setProperty("value", self.c4("Feedback.txt"))
        self.progressBar_4.setProperty("value",self.c3("Feedback.txt"))
        self.progressBar_5.setProperty("value", self.c2("Feedback.txt"))
        self.progressBar_6.setProperty("value", self.c1("Feedback.txt"))

    def Save_button_function(self):
        fb = self.textEdit.toPlainText()
        f = open('Feedback.txt', 'wt')
        f.write(fb)
        f.close()





 #   def feedback_view():
  #      global feedback_ui
  #      feedback_ui = Ui_MainWindow4()
  #      feedback_ui.setupUi(MainWindow)
  #      feedback_ui.tabWidget.setCurrentWidget(feedback_ui.feedback)

   #     feedback_ui.pushButton_2.clicked.connect(review_main_menu)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    waiter_ui = Feedback()
    waiter_ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())