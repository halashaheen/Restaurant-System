# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!
import sys

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)
mycursor = mydb.cursor()

from PyQt5 import QtCore, QtGui, QtWidgets


class Cashier(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMinimumSize(QtCore.QSize(200, 0))
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_3.addWidget(self.pushButton_13)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda :self.addNewItemTodatabase())
        self.pushButton_3.clicked.connect(lambda :self.UpdateQuantity())
        self.pushButton_2.clicked.connect(lambda :self.GetWordToFind())
        self.pushButton_13.clicked.connect(lambda :self.Total())
        self.comboBox.activated.connect(lambda :self.addrow())
        self.pushButton_5.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cashier "))
        self.groupBox_2.setTitle(_translate("MainWindow", "Find Item"))
        self.pushButton_2.setText(_translate("MainWindow", "Find"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Total"))
        self.label_3.setText(_translate("MainWindow", "Quantity"))
        self.pushButton_3.setText(_translate("MainWindow", "update"))
        self.pushButton_13.setText(_translate("MainWindow", "T o t a l"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "Add Item"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_2.setText(_translate("MainWindow", "Price"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_4.setText(_translate("MainWindow", "Back to Main Menu"))
        self.pushButton_5.setText(_translate("MainWindow", "close"))

    def addrow(self):
        # change row count
        count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(count + 1)
        # adjust row header
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(count, item)
        it = self.tableWidget.verticalHeaderItem(count)
        it.setText(str(count + 1))
        # adjust item name
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(count, 0, item)
        item = self.tableWidget.item(count, 0)
        item_name = self.comboBox.currentText()
        item.setText(item_name)
        # adjust price
        sql = "SELECT price FROM menu WHERE name = '{}' "
        sql = sql.format(item_name)
        mycursor.execute(sql)
        data = mycursor.fetchone()
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(count, 1, item)
        item = self.tableWidget.item(count, 1)
        item.setText(data[0])
        # default Quantity
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(count, 2, item)
        item = self.tableWidget.item(count, 2)
        item.setText("1")

    def Display_Total_price(self,sum):
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(0)
        st = "Food Price  :    {}"
        st = st.format(str(sum))
        item.setText(st)
        item = self.listWidget.item(1)
        st = "Taxes&service: {}"

        st = st.format(str(int((sum * 0.28))))
        item.setText(st)
        item = self.listWidget.item(2)
        st = "Total Price  : {}"

        st = st.format(str(int(sum * 1.28)))
        item.setText(st)

    def Total(self):
        sum = 0
        for x in range(self.tableWidget.rowCount()):
            item1 = self.tableWidget.item(x, 1)
            item2 = self.tableWidget.item(x, 2)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(x, 3, item)
            item3 = self.tableWidget.item(x, 3)
            pr = int(item1.text()) * int(item2.text())
            sum = sum + pr
            item3.setText(str(pr))
        self.Display_Total_price(sum)




    def UpdateQuantity(self):
        count = self.tableWidget.rowCount()
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(count - 1, 2, item)
        item = self.tableWidget.item(count - 1, 2)
        item.setText(self.spinBox.text())




    def UpdateDropBoxFromDataBase(self,var):
        mycursor.execute("SELECT name from Menu")
        s = []
        a = []
        for x in mycursor:
            s.append(x)
        h = 0
        for i in s:
            s[h] = str(i).strip("()',")
            h = h + 1
        for i in s:
            x = var in i
            if x == 1:
                a.append(i)
        sql = "SELECT * FROM menu WHERE name='{}'"
        for x in a:
            e = sql.format(x)
            mycursor.execute(e)
            myresult = mycursor.fetchall()
            stu = myresult[0][1]
            self.comboBox.addItem(stu)


    def GetWordToFind(self):
        self.comboBox.clear()
        var = self.lineEdit_3.text()
        self.lineEdit_3.clear()
        self.UpdateDropBoxFromDataBase(var)


    def addNewItemTodatabase(self):
        name = self.lineEdit.text()
        price = self.lineEdit_2.text()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        sql = "INSERT INTO MENU (name,price) VALUES ( %s, %s  )"
        val = (name, price)
        mycursor.execute(sql, val)
        mydb.commit()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Cashier()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())