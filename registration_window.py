from PyQt5 import QtCore, QtGui, QtWidgets
import connect_to_database as ctd
import functools



class Ui_reg_window(object):
    def setupUi(self, reg_window):
        reg_window.setObjectName("reg_window")
        reg_window.resize(602, 442)
        font = QtGui.QFont()
        font.setPointSize(15)
        reg_window.setFont(font)

        self.buttonBox = QtWidgets.QDialogButtonBox(reg_window)
        self.buttonBox.setGeometry(QtCore.QRect(380, 400, 201, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.label = QtWidgets.QLabel(reg_window)
        self.label.setGeometry(QtCore.QRect(60, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.name_lineEdit = QtWidgets.QLineEdit(reg_window)
        self.name_lineEdit.setGeometry(QtCore.QRect(220, 40, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setObjectName("name_lineEdit")

        self.post_lineEdit = QtWidgets.QLineEdit(reg_window)
        self.post_lineEdit.setGeometry(QtCore.QRect(220, 110, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.post_lineEdit.setFont(font)
        self.post_lineEdit.setObjectName("post_lineEdit")

        self.label_2 = QtWidgets.QLabel(reg_window)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.email_lineEdit = QtWidgets.QLineEdit(reg_window)
        self.email_lineEdit.setGeometry(QtCore.QRect(220, 180, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setObjectName("email_lineEdit")

        self.label_3 = QtWidgets.QLabel(reg_window)
        self.label_3.setGeometry(QtCore.QRect(60, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.password_lineEdit = QtWidgets.QLineEdit(reg_window)
        self.password_lineEdit.setGeometry(QtCore.QRect(220, 250, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.label_4 = QtWidgets.QLabel(reg_window)
        self.label_4.setGeometry(QtCore.QRect(60, 260, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.error_label = QtWidgets.QLabel(reg_window)
        self.error_label.setGeometry(QtCore.QRect(30, 320, 541, 61))
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")

        self.retranslateUi(reg_window)
        self.buttonBox.accepted.connect(functools.partial(self.registration, reg_window)) # type: ignore

        self.buttonBox.rejected.connect(reg_window.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(reg_window)


    def retranslateUi(self, reg_window):
        _translate = QtCore.QCoreApplication.translate
        reg_window.setWindowTitle(_translate("reg_window", "Регистрация"))
        self.label.setText(_translate("reg_window", "Имя"))
        self.label_2.setText(_translate("reg_window", "Должность"))
        self.label_3.setText(_translate("reg_window", "Email"))
        self.label_4.setText(_translate("reg_window", "Password"))


    def registration(self, reg_window):
        name = self.name_lineEdit.text()
        post = self.post_lineEdit.text()
        mail = self.email_lineEdit.text()
        password = self.password_lineEdit.text()
        error_message = ''
        if not ctd.registration_valid(email=mail):
            error_message += 'Эта почта уже занята\n'

        if ' ' in password or len(password) == 0:
            error_message += 'Некорректный пароль\n'


        self.error_label.setText(error_message)

        if len(error_message) == 0:
            ctd.create_account(name, post, mail, password)
            print('yes')
            reg_window.accept()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # reg_window = QtWidgets.QDialog()
    # ui = Ui_reg_window()
    # ui.setupUi(reg_window)
    # reg_window.show()
    sys.exit(app.exec_())
