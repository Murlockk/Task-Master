from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        self.layout = QtWidgets.QVBoxLayout(Dialog)

        self.title_input = QtWidgets.QLineEdit(Dialog)
        self.title_input.setPlaceholderText("Название задачи")
        self.layout.addWidget(self.title_input)

        self.description_input = QtWidgets.QTextEdit(Dialog)
        self.description_input.setPlaceholderText("Описание задачи")
        self.layout.addWidget(self.description_input)

        self.button_box = QtWidgets.QDialogButtonBox(Dialog)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(Dialog.accept)
        self.button_box.rejected.connect(Dialog.reject)

    def get_data(self):
        return self.title_input.text(), self.description_input.toPlainText()


class Ui_MainWindow(object):
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

        # Кнопка добавления задачи
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setText("Добавить задачу")
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)

        # Кнопка удаления задачи
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setText("Удалить задачу")
        self.delete_button.setObjectName("delete_button")
        self.verticalLayout.addWidget(self.delete_button)

        # Кнопка просмотра задачи
        self.view_button = QtWidgets.QPushButton(self.centralwidget)
        self.view_button.setText("Просмотреть задачу")
        self.view_button.setObjectName("view_button")
        self.verticalLayout.addWidget(self.view_button)

        self.add_button.clicked.connect(self.button_clicked)
        self.delete_button.clicked.connect(self.delete_task)
        self.view_button.clicked.connect(self.view_task)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.horizontalLayout.addLayout(self.verticalLayout)

        # Создание первого QScrollArea
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # виджет для содержимого первого ScrollArea
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #  первый ScrollArea
        self.vbox = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        # Создание Tree Widget
        self.tree = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)
        self.tree.setHeaderLabels(["Название", "Описание"])

        # Пример корневого элемента
        task_group = QtWidgets.QTreeWidgetItem(self.tree)
        task_group.setText(0, "Задачи")

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

        # Добавление дерева в 2ом qscrollArea
        self.vbox.addWidget(self.tree)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.second_scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.second_scroll_area.setWidgetResizable(True)
        self.second_scroll_area.setObjectName("second_scroll_area")

        self.second_scroll_area_widget_contents = QtWidgets.QWidget()
        self.second_scroll_area_widget_contents.setObjectName("second_scroll_area_widget_contents")

        self.second_vbox = QtWidgets.QVBoxLayout(self.second_scroll_area_widget_contents)

        self.task_info_display = QtWidgets.QTextEdit(self.second_scroll_area_widget_contents)
        self.task_info_display.setReadOnly(True)
        self.second_vbox.addWidget(self.task_info_display)

        self.second_scroll_area.setWidget(self.second_scroll_area_widget_contents)
        self.horizontalLayout.addWidget(self.second_scroll_area)

        MainWindow.setCentralWidget(self.centralwidget)
        self.tree.itemDoubleClicked.connect(self.view_task_on_double_click)

    def button_clicked(self):
        dialog = QtWidgets.QDialog()

        dialog_ui = Ui_Dialog()
        dialog_ui.setupUi(dialog)

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            title, description = dialog_ui.get_data()
            if title and description:
                self.add_task_to_tree(title, description)

    def add_task_to_tree(self, title, description):

        task_group = self.tree.findItems("Задачи", QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)[0]

        task_item = QtWidgets.QTreeWidgetItem(task_group)

        task_item.setText(0, title)
        task_item.setText(1, description)

    def delete_task(self):
        selected_items = self.tree.selectedItems()


        print(selected_items)

        if selected_items:
            for item in selected_items:
                index = self.tree.indexOfTopLevelItem(item)
                if index != -1:
                    self.tree.takeTopLevelItem(index)
                else:
                    parent = item.parent()
                    if parent:
                        index = parent.indexOfChild(item)
                        parent.removeChild(item)

    def view_task(self):
        selected_items = self.tree.selectedItems()

        if selected_items:
            item = selected_items[0]
            title = item.text(0)
            description = item.text(1)

            task_info = f"Название: {title}\n\nОписание: {description}"
            self.task_info_display.setPlainText(task_info)

    def view_task_on_double_click(self, item):
        path_list = []
        current_item = item

        while current_item is not None:
            path_list.append(current_item.text(0))
            current_item = current_item.parent()

        path_list.reverse()

        if len(path_list) > 1:
            project_name = path_list[-2]
            task_name = path_list[-1]
        else:
            project_name = "Задачи"
            task_name = path_list[0] if path_list else "Неизвестная задача"

        description = item.text(1)

        task_info = f"Проект: {project_name}\nЗадача: {task_name}\n\nОписание: {description}"
        self.task_info_display.setPlainText(task_info)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
