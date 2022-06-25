from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import res , sys, os
import database
from information import Ui_infoWindow
import shutil
import Main_face_compare

class Ui_SecondWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_infoWindow() 
        self.ui.setupUi(self.window)   
        self.window.show()
    
         
    def __init__(self) -> None:
        self.db = database.DB()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1011, 721))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color : qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"    color: rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color : qlineargradient(spread:pad,x1:0,y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color : rgba(150,123,111,255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 851, 621))
        self.label_2.setStyleSheet("background-color : rgba(50,50,50,255);\n"
"border-radius : 50px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.clicked.connect(self.openWindow)
        self.pushButton.setGeometry(QtCore.QRect(350, 490, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 410, 351, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(360, 320, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color : rgb(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "send"))
        self.pushButton.clicked.connect(self.find_person)
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Passport Number"))
        self.label_3.setText(_translate("MainWindow", "Enter Passport"))
    def find_person(self):
        self.passport_ID = self.lineEdit_2.text()
        passportInfo = self.db.get_passport(self.passport_ID).__dict__
        lableText = f"""
                First Name : {passportInfo['first_name']}
                Last Name : {passportInfo['last_name']}
                Father's Name : {passportInfo['father_name']}
                Date of Birth : {passportInfo['date_of_birth']}
                Place of Birth : {passportInfo['place_of_birth']}
                Date of issue : {passportInfo['date_of_issue']}
                Date of Expiry : {passportInfo['date_of_expiry']}
                Gender : {"Male" if passportInfo['gender'] == 'M' else "Female"}
                Passport No. : {passportInfo['passport_number']}
        """
        
        self.ui.label.setText(lableText)
        self.path = os.path.dirname(os.path.abspath(__file__)) + '\\img\\' + passportInfo['picture']
        pixmap = QPixmap(self.path)
        self.ui.picLabel.setPixmap(pixmap)

        shutil.copy(self.path, os.path.dirname(os.path.abspath(__file__)) + '\\img\\passenger.jpg')

        out,confidence = Main_face_compare.main(passportInfo['first_name'] + ' ' + passportInfo['last_name'])
        print(f' output percentage and final condition is : {out} , {confidence}')

        self.ui.label.setText(f"""
            {self.ui.label.text()}
            Output : {"True" if out else "False"}
            Confidence : {confidence}
        """)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_SecondWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
 
