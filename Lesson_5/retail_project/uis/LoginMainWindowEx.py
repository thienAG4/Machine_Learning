from PyQt6.QtWidgets import QMessageBox
from Lesson_5.retail_project.connectors.employee_connector import EmployeeConnector
from Lesson_5.retail_project.uis.LoginMainWindow import Ui_MainWindow


class LoginMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)


    def process_login(self):
        email = self.lineEditEmail.text()
        pwd = self.lineEditPassword.text()
        ec = EmployeeConnector()
        ec.connect()
        em = ec.login(email, pwd)
        if em == None:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login Fail, please check your account again")
            msg.setWindowTitle("Login Failed")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Siuuuu! Login Successful!!!")
            msg.setWindowTitle("Login ok ok")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()