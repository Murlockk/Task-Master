from PyQt5 import QtCore, QtGui, QtWidgets
import connect_to_database as ctd
import registration_window


class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(425, 283)
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")

        self.login_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_lineEdit.setGeometry(QtCore.QRect(132, 40, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setObjectName("login_lineEdit")

        self.password_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_lineEdit.setGeometry(QtCore.QRect(132, 80, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignRight)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignRight)

        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(10, 120, 500, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.error_label.setFont(font)
        self.error_label.setObjectName("error_label")

        self.registration_button = QtWidgets.QPushButton(self.centralwidget)
        self.registration_button.setGeometry(QtCore.QRect(50, 180, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.registration_button.setFont(font)
        self.registration_button.setObjectName("registration_button")

        self.registration_button.clicked.connect(self.reg_but)

        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(230, 180, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        login_window.setCentralWidget(self.centralwidget)

        self.login_button.clicked.connect(self.login_but)

        self.menubar = QtWidgets.QMenuBar(login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 26))
        self.menubar.setObjectName("menubar")
        login_window.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(login_window)
        self.statusbar.setObjectName("statusbar")
        login_window.setStatusBar(self.statusbar)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "Добро пожаловать"))
        self.label.setText(_translate("login_window", "Email:"))
        self.label_2.setText(_translate("login_window", "Password:"))
        self.registration_button.setText(_translate("login_window", "Регистрация"))
        self.login_button.setText(_translate("login_window", "Вход"))


    def login_but(self):
        login = self.login_lineEdit.text()
        password = self.password_lineEdit.text()
        if ctd.login_in_account(login=login,
                                password=password):
            print(ctd.login_in_account(login=login,
                                       password=password))
            # login_window.close()
        else:
            self.error_label.setText('Неверный email или пароль')

    def reg_but(self):
        print('reg')
        self.reg_window = QtWidgets.QDialog()
        self.reg_ui = registration_window.Ui_reg_window()
        self.reg_ui.setupUi(self.reg_window)
        self.reg_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = Ui_login_window()
    ui.setupUi(login_window)
    login_window.show()
    sys.exit(app.exec_())
