import sys
import unittest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from add import Cashier
app = QApplication(sys.argv)
class Table_Reservation_Test(unittest.TestCase):


    def setUp(self):

        self.form = Cashier()
        self.form.setupUi(QtWidgets.QMainWindow())

    def test_defaults(self):

        self.assertEqual(self.form.lineEdit_1.text(),"")
        self.assertEqual(self.form.lineEdit_3.text(), "")
        self.assertEqual(self.form.lineEdit_6.text(), "")
        self.assertEqual(self.form.lineEdit_7.text(), "")


    def test_buttons(self):
        self.form.lineEdit_6.setText('omar')
        self.form.lineEdit_7.setText('1')
        self.form.lineEdit_3.setText('123')
        self.form.pushButton_6.click()
        self.assertTrue(self.form.tableWidget.item(0,0))
        self.form.lineEdit_7.setText('1')
        self.form.pushButton_5.click()
        self.assertFalse(self.form.tableWidget.item(0,0))



if __name__ == "__main__":
    unittest.main()