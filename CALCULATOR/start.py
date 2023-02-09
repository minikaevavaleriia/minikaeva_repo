import sys
import os
from pathlib import Path

from PyQt6.QtCore import QDir
from PyQt6.QtGui import QIcon, QPalette, QBrush
from PyQt6.QtCore import QSize, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout

from CALCULATOR.act_but import ActionButton
from CALCULATOR.num_but import NumberButton

CURRENT_DIRECTORY = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # окно
        self.setWindowTitle("INSTACALC")
        self.setFixedSize(QSize(720, 720))
        self.setContentsMargins(10, 20, 10, 20)


        # дисплей
        self.label = QLabel('Введите значение')
        self.label.setStyleSheet('background-color: lightpink;'
                                 'border: 1px solid black;')
        self.label.setFixedSize(680, 100)
        self.label.move(-300, 0)


        #цифры
        self.number_1 = NumberButton('1', 1, self.label)
        self.number_1.setFixedSize(175, 50)
        self.number_1.clicked.connect(lambda: self.number_was_clicked(self.number_1))

        self.number_2 = NumberButton('2', 2, self.label)
        self.number_2.setFixedSize(175, 50)
        self.number_2.clicked.connect(lambda: self.number_was_clicked(self.number_2))

        self.number_3 = NumberButton('3', 3, self.label)
        self.number_3.setFixedSize(175, 50)
        self.number_3.clicked.connect(lambda: self.number_was_clicked(self.number_3))

        self.number_4 = NumberButton('4', 4, self.label)
        self.number_4.setFixedSize(175, 50)
        self.number_4.clicked.connect(lambda: self.number_was_clicked(self.number_4))

        self.number_5 = NumberButton('5', 5, self.label)
        self.number_5.setFixedSize(175, 50)
        self.number_5.clicked.connect(lambda: self.number_was_clicked(self.number_5))

        self.number_6 = NumberButton('6', 6, self.label)
        self.number_6.setFixedSize(175, 50)
        self.number_6.clicked.connect(lambda: self.number_was_clicked(self.number_6))

        self.number_7 = NumberButton('7', 7, self.label)
        self.number_7.setFixedSize(175, 50)
        self.number_7.clicked.connect(lambda: self.number_was_clicked(self.number_7))

        self.number_8 = NumberButton('8', 8, self.label)
        self.number_8.setFixedSize(175, 50)
        self.number_8.clicked.connect(lambda: self.number_was_clicked(self.number_8))

        self.number_9 = NumberButton('9', 9, self.label)
        self.number_9.setFixedSize(175, 50)
        self.number_9.clicked.connect(lambda: self.number_was_clicked(self.number_9))

        self.number_0 = NumberButton('0', 0, self.label)
        self.number_0.setFixedSize(175, 50)
        self.number_0.clicked.connect(lambda: self.number_was_clicked(self.number_0))


        #кнопки с действиями
        self.action_AC = ActionButton('AC', 'del', self.label)
        self.action_AC.setFixedSize(175, 50)
        self.action_AC.clicked.connect(lambda: self.action_was_clicked(self.action_AC))

        self.action_MS = ActionButton('MS', 'save', self.label)
        self.action_MS.setFixedSize(175, 50)
        self.action_MS.clicked.connect(lambda: self.action_was_clicked(self.action_MS))

        self.action_power = ActionButton('^', 'pow', self.label)
        self.action_power.setFixedSize(175, 50)
        self.action_power.clicked.connect(lambda: self.action_was_clicked(self.action_power))

        self.action_div = ActionButton('/', 'div', self.label)
        self.action_div.setFixedSize(175, 50)
        self.action_div.clicked.connect(lambda: self.action_was_clicked(self.action_div))

        self.action_multiply = ActionButton('*', 'multiply', self.label)
        self.action_multiply.setFixedSize(175, 50)
        self.action_multiply.clicked.connect(lambda: self.action_was_clicked(self.action_multiply))

        self.action_sub = ActionButton('-', 'sub', self.label)
        self.action_sub.setFixedSize(175, 50)
        self.action_sub.clicked.connect(lambda: self.action_was_clicked(self.action_sub))

        self.action_add = ActionButton('+', 'add', self.label)
        self.action_add.setFixedSize(175, 50)
        self.action_add.clicked.connect(lambda: self.action_was_clicked(self.action_add))

        self.action_eq = ActionButton('=', 'eq', self.label)
        self.action_eq.setFixedSize(175, 50)
        self.action_eq.clicked.connect(lambda: self.action_was_clicked(self.action_eq))

        self.action_MR = ActionButton('MR', 'insert', self.label)
        self.action_MR.setFixedSize(175, 50)
        self.action_MR.clicked.connect(lambda: self.action_was_clicked(self.action_MR))

        self.action_dot = ActionButton('.', 'dot', self.label)
        self.action_dot.setFixedSize(175, 50)
        self.action_dot.clicked.connect(lambda: self.action_was_clicked(self.action_dot))


        #кнопки с цифрами располагаю
        self.layout = QGridLayout()

        # добавляю дисплей
        self.layout.addWidget(self.label, 0, 0)

        # расставляю цифры
        self.layout.addWidget(self.number_7, 2, 0, 1, 1)
        self.layout.addWidget(self.number_8, 2, 1, 1, 1)
        self.layout.addWidget(self.number_9, 2, 2, 1, 1)

        self.layout.addWidget(self.number_4, 3, 0)
        self.layout.addWidget(self.number_5, 3, 1)
        self.layout.addWidget(self.number_6, 3, 2)

        self.layout.addWidget(self.number_1, 4, 0)
        self.layout.addWidget(self.number_2, 4, 1)
        self.layout.addWidget(self.number_3, 4, 2)

        self.layout.addWidget(self.number_0, 5, 1)


        # расставляю кнопки с действиями
        self.layout.addWidget(self.action_AC, 1,  0)
        self.layout.addWidget(self.action_MS, 1,  1)
        self.layout.addWidget(self.action_power, 1, 2)
        self.layout.addWidget(self.action_div, 1, 3)

        self.layout.addWidget(self.action_multiply, 2, 3)
        self.layout.addWidget(self.action_sub, 3, 3)
        self.layout.addWidget(self.action_add, 4, 3)
        self.layout.addWidget(self.action_eq, 5, 3)

        self.layout.addWidget(self.action_MR, 5, 0)
        self.layout.addWidget(self.action_dot, 5, 2)
        self.layout.addWidget(self.action_MR, 5, 3)

        # создаю контейнер, в него лейаут и контейнер - центральный виджет
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)




    @pyqtSlot()
    def number_was_clicked(self, button):
        button.label.setText(button.text())
        print(f'{button.val} pushed!')

    @pyqtSlot()
    def action_was_clicked(self, button):
        button.label.setText(button.text())
        print(f'{button.val} pushed!')

def main():
    app = QApplication(sys.argv)

    QDir.addSearchPath("icons", os.fspath(CURRENT_DIRECTORY / "icons"))
    icon = QIcon("icons:myicon.png")
    assert not icon.isNull()

    window = MainWindow()
    window.setWindowIcon(icon)
    window.show()

    app.setStyleSheet("""
        QWidget {
            background-color: "pink";
            color: "black";
        }
        QPushButton {
            font-size: 16px;
            background-color: "lightpink"
        }
        MainWindow {
            background-color: "white";
        }
    """)


    sys.exit(app.exec())

if __name__ == "__main__":
    main()