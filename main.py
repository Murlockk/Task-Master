from PyQt5 import QtCore, QtGui, QtWidgets

from create_new_task import Ui_Dialog


class Ui_MainWindow(object):
    user_name = ''
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1192, 819)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.user_name_label = QtWidgets.QLabel(self.centralwidget)
        self.user_name_label.setText('HELLO WORLD')
        self.user_name_label.setObjectName('user_name_label')
        self.verticalLayout.addWidget(self.user_name_label)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName('like')

        self.verticalLayout.addWidget(self.button)
        self.pushButton.clicked.connect(self.add_buttons)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 529, 744))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()


        # ПРИМЕР TREE WIDGET
        # Создание Tree Widget
        self.tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree.setHeaderLabels(["Название", "Описание"])  # Заголовки колонок

        # Пример корневого элемента
        task_group = QtWidgets.QTreeWidgetItem(self.tree)
        task_group.setText(0, "Задачи")  # Колонка 0 — Название

        # Подзадачи
        task1 = QtWidgets.QTreeWidgetItem(task_group)
        task1.setText(0, "Сделать домашку")
        task1.setText(1, "По математике")

        task2 = QtWidgets.QTreeWidgetItem(task_group)
        task2.setText(0, "Прочитать статью")
        task2.setText(1, "Про PyQt")

        # Второй корень
        project_group = QtWidgets.QTreeWidgetItem(self.tree)
        project_group.setText(0, "Проекты")

        project1 = QtWidgets.QTreeWidgetItem(project_group)
        project1.setText(0, "Сделать UI")
        project1.setText(1, "Интерфейс с кнопками и TreeView")

        # Добавление в layout
        self.vbox.addWidget(self.tree)

        # Обновим ScrollArea
        self.widget.setLayout(self.vbox)
        self.scrollArea.setWidget(self.widget)

        # КОНЕЦ ПРИМЕРА


        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 528, 744))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.widget2 = QtWidgets.QWidget()
        self.vbox2 = QtWidgets.QVBoxLayout()

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1192, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Добавить задачу"))
        self.button.setText(_translate("MainWindow", "Hello"))


    def add_buttons(self):
        title, description = self.create_task()
        if title and description:
            name = QtWidgets.QPushButton(title)
            name.clicked.connect(lambda: self.show_full_task(name=title,
                                                             text=description))
            btn = QtWidgets.QPushButton('something')
            container = QtWidgets.QHBoxLayout()
            container.addWidget(name)
            container.addWidget(btn)
            self.vbox.addLayout(container)
            self.widget.setLayout(self.vbox)
            self.scrollArea.setWidget(self.widget)


    def create_task(self):
        dialog = QtWidgets.QDialog()
        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            title, description = dialog_ui.get_data()
            return title, description
        return None, None


    def show_full_task(self, name, text):

        while self.vbox2.count():
            item = self.vbox2.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        label = QtWidgets.QLabel(name)
        task = QtWidgets.QTextBrowser()
        task.setText(text)
        self.vbox2.addWidget(label)
        self.vbox2.addWidget(task)
        self.widget2.setLayout(self.vbox2)
        self.scrollArea_2.setWidget(self.widget2)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
