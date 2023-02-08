import sys

from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QGridLayout

from CALCULATOR.num_but import NumberButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("INSTACALC")
        self.setFixedSize(QSize(720, 720))
        self.setContentsMargins(10, 20, 10, 20)

        # дисплей
        self.label = QLabel('Введите значение')
        self.label.setStyleSheet('background-color: pink;'
                                 'border: 1px solid black;')
        self.label.setFixedSize(680, 100)
        self.label.move(-300, 0)


        #цифры
        self.number_1 = NumberButton('1', 1, self.label)
        self.number_1.setFixedSize(175, 50)
        self.number_1.clicked.connect(self.the_number1_was_clicked)

        self.number_2 = NumberButton('2', 2, self.label)
        self.number_2.setFixedSize(175, 50)
        self.number_2.clicked.connect(self.the_number2_was_clicked)

        self.number_3 = NumberButton('3', 3, self.label)
        self.number_3.setFixedSize(175, 50)
        self.number_3.clicked.connect(self.the_number3_was_clicked)

        self.number_4 = NumberButton('4', 4, self.label)
        self.number_4.setFixedSize(175, 50)
        self.number_4.clicked.connect(self.the_number4_was_clicked)

        self.number_5 = NumberButton('5', 5, self.label)
        self.number_5.setFixedSize(175, 50)
        self.number_5.clicked.connect(self.the_number5_was_clicked)

        self.number_6 = NumberButton('6', 6, self.label)
        self.number_6.setFixedSize(175, 50)
        self.number_6.clicked.connect(self.the_number6_was_clicked)

        self.number_7 = NumberButton('7', 7, self.label)
        self.number_7.setFixedSize(175, 50)
        self.number_7.clicked.connect(self.the_number7_was_clicked)

        self.number_8 = NumberButton('8', 8, self.label)
        self.number_8.setFixedSize(175, 50)
        self.number_8.clicked.connect(self.the_number8_was_clicked)

        self.number_9 = NumberButton('9', 9, self.label)
        self.number_9.setFixedSize(175, 50)
        self.number_9.clicked.connect(self.the_number9_was_clicked)

        self.number_0 = NumberButton('0', 0, self.label)
        self.number_0.setFixedSize(175, 50)
        self.number_0.clicked.connect(self.the_number0_was_clicked)

        #действия кнопки

        #кнопки с цифрами располагаю
        self.layout = QGridLayout()
        # добавляю дисплей
        self.layout.addWidget(self.label, 0, 0)

        self.layout.addWidget(QPushButton('ok'), 1, 0)
        self.layout.addWidget(QPushButton('ok'), 1, 1)
        self.layout.addWidget(QPushButton('ok'), 1, 2)
        self.layout.addWidget(QPushButton('ok'), 1, 3)

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

        self.layout.addWidget(QPushButton('ok'), 5, 0)
        self.layout.addWidget(QPushButton('ok'), 5, 2)
        self.layout.addWidget(QPushButton('ok'), 5, 3)

        self.layout.addWidget(QPushButton('ok'), 2, 3)
        self.layout.addWidget(QPushButton('ok'), 3, 3)
        self.layout.addWidget(QPushButton('ok'), 4, 3)


        self.container = QWidget()
        self.container.setLayout(self.layout)


        self.setCentralWidget(self.container)

    @pyqtSlot()
    def the_number1_was_clicked(self):
        self.label.setText(self.number_1.text())
        print(f'{self.number_1.val}pushed!')

    def the_number2_was_clicked(self):
        self.label.setText(self.number_2.text())
        print(f'{self.number_2.val}pushed!')

    def the_number3_was_clicked(self):
        self.label.setText(self.number_3.text())
        print(f'{self.number_3.val}pushed!')

    def the_number4_was_clicked(self):
        self.label.setText(self.number_4.text())
        print(f'{self.number_4.val}pushed!')

    def the_number5_was_clicked(self):
        self.label.setText(self.number_5.text())
        print(f'{self.number_5.val}pushed!')

    def the_number6_was_clicked(self):
        self.label.setText(self.number_6.text())
        print(f'{self.number_6.val}pushed!')

    def the_number7_was_clicked(self):
        self.label.setText(self.number_7.text())
        print(f'{self.number_7.val}pushed!')

    def the_number8_was_clicked(self):
        self.label.setText(self.number_8.text())
        print(f'{self.number_8.val}pushed!')

    def the_number9_was_clicked(self):
        self.label.setText(self.number_9.text())
        print(f'{self.number_9.val}pushed!')

    def the_number0_was_clicked(self):
        self.label.setText(self.number_0.text())
        print(f'{self.number_0.val}pushed!')



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()