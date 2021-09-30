import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QApplication
from PyQt6.QtGui import QIcon, QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.position_n_size()
        self.setWindowTitle('Organize me')
        self.statusBar()
        self.menu_create()
        self.toolbar_create()
        self.show()

    def position_n_size(self):
        self.resize(550, 550)
        self.center_me()

    def center_me(self):
        screen_center = self.screen().availableGeometry().center()
        frame = self.frameGeometry()
        frame.moveCenter(screen_center)
        self.move(frame.topLeft())

    def toolbar_create(self):
        # toolbar0 = self.addToolBar('New')
        toolbar1 = self.addToolBar('Toolbar')
        toolbar1.addAction(self.exit_me())
        toolbar1.addAction(self.new_file())

    def menu_create(self):
        my_menu = self.menuBar()
        main_menu = my_menu.addMenu('&Функции')
        main_menu.addAction(self.exit_me())
        main_menu.addAction(self.new_file())

    def exit_me(self):
        exit_act = QAction(QIcon('../img/exit.png'), 'Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.setStatusTip('Exit app')
        exit_act.triggered.connect(self.close)
        return exit_act

    def new_file(self):
        new_file_act = QAction(QIcon('../img/new_item.jpg'), 'New file', self)
        new_file_act.setShortcut('Ctrl+N')
        new_file_act.setStatusTip('Create new item')
        return new_file_act
        # new_file_act.triggered.connect(self.) # создать новую запись в категории


def main():

    app = QApplication(sys.argv)
    my_example = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
