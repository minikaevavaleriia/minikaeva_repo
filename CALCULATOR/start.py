import sys
import os
from pathlib import Path

import re

from PyQt6.QtCore import QDir, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout

from CALCULATOR.act_but import ActionButton
from CALCULATOR.num_but import NumberButton

CURRENT_DIRECTORY = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.memory = []


        self.setMouseTracking(True)
        # окно
        self.setWindowTitle("INSTACALC")
        self.setFixedSize(QSize(720, 720))

        # дисплей
        self.result = '0'
        self.label_result = QLabel(self.result)
        self.label_result.setFixedSize(520, 100)
        self.label_result.setAlignment(Qt.AlignmentFlag.AlignCenter)


        #цифры
        self.number_1 = NumberButton('1', 1)
        self.number_1.clicked.connect(lambda: self.number_was_clicked(self.number_1.name))

        self.number_2 = NumberButton('2', 2)
        self.number_2.clicked.connect(lambda: self.number_was_clicked(self.number_2.name))

        self.number_3 = NumberButton('3', 3)
        self.number_3.clicked.connect(lambda: self.number_was_clicked(self.number_3.name))

        self.number_4 = NumberButton('4', 4)
        self.number_4.clicked.connect(lambda: self.number_was_clicked(self.number_4.name))

        self.number_5 = NumberButton('5', 5)
        self.number_5.clicked.connect(lambda: self.number_was_clicked(self.number_5.name))

        self.number_6 = NumberButton('6', 6)
        self.number_6.clicked.connect(lambda: self.number_was_clicked(self.number_6.name))

        self.number_7 = NumberButton('7', 7)
        self.number_7.clicked.connect(lambda: self.number_was_clicked(self.number_7.name))

        self.number_8 = NumberButton('8', 8)
        self.number_8.clicked.connect(lambda: self.number_was_clicked(self.number_8.name))

        self.number_9 = NumberButton('9', 9)
        self.number_9.clicked.connect(lambda: self.number_was_clicked(self.number_9.name))

        self.number_0 = NumberButton('0', 0)
        self.number_0.clicked.connect(lambda: self.number_was_clicked(self.number_0.name))


        #кнопки с действиями
        self.action_AC = ActionButton('AC', 'del')
        self.action_AC.clicked.connect(lambda: self.number_was_clicked(self.action_AC.name))

        self.action_MS = ActionButton('MS', 'save')
        self.action_MS.clicked.connect(lambda: self.memory_save(self.action_MS.name))

        self.action_power = ActionButton('^', 'pow')
        self.action_power.clicked.connect(lambda: self.number_was_clicked(self.action_power.name))

        self.action_div = ActionButton('/', 'div')
        self.action_div.clicked.connect(lambda: self.number_was_clicked(self.action_div.name))

        self.action_multiply = ActionButton('*', 'multiply')
        self.action_multiply.clicked.connect(lambda: self.number_was_clicked(self.action_multiply.name))

        self.action_sub = ActionButton('-', 'sub')
        self.action_sub.clicked.connect(lambda: self.number_was_clicked(self.action_sub.name))

        self.action_add = ActionButton('+', 'add')
        self.action_add.clicked.connect(lambda: self.number_was_clicked(self.action_add.name))

        self.action_eq = ActionButton('=', 'eq')
        self.action_eq.clicked.connect(lambda: self.equals())

        self.action_MR = ActionButton('MR', 'insert')
        self.action_MR.clicked.connect(lambda: self.memory_read(self.action_MR))

        self.action_dot = ActionButton('.', 'dot')
        self.action_dot.clicked.connect(lambda: self.dot(self.action_dot))


        #кнопки с цифрами располагаю
        self.layout = QGridLayout()

        # добавляю дисплей
        # self.layout.addWidget(self.input)
        self.layout.addWidget(self.label_result)

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

        #РАССТОЯНИЕ МЕЖДУ ЭЛЕМЕНТАМИ И ПИКСЕЛИ ОТ КРАЕВ ДО СЛОЯ НЕ ТРОГАААААТЬ!!!
        self.layout.setContentsMargins(100, 52, 100, 40)
        self.layout.setHorizontalSpacing(53)

        # создаю контейнер, в него лейаут и контейнер - центральный виджет
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

    def number_was_clicked(self, button):  # вывод цифры на кнопке на экран
        if button == 'AC':
            self.label_result.setText(f'0')
        else:
            if self.label_result.text() == "0":
                self.label_result.setText("")

            self.label_result.setText(f'{self.label_result.text()}{button}')

        print(f'{button} pushed!')

    def equals(self):
        screen = self.label_result.text()
        power_checked = check_power(screen)
        print('!!!' + power_checked)

        try:
            answer = eval(power_checked)
            print(answer)
            self.label_result.setText(str(answer))

        except:
            self.label_result.setText("ERROR")

    def dot(self, button):
        screen = self.label_result.text()
        if screen[-1] == ".":
            pass
        else:
            self.label_result.setText(f'{screen}.')
        print(f'{button} pushed!')

    def memory_save(self, button):
        screen = self.label_result.text()
        if re.match('\d+', screen):
            if not self.memory:
                self.memory.append(screen)
            else:
                self.label_result.setText("MEMORY IS FULL")
        print(f'{button} pushed!')

    def memory_read(self, button):
        screen = self.label_result.text()
        if self.memory:
            self.label_result.setText(f'{screen}{self.memory.pop()}')
        else:
            self.label_result.setText("MEMORY IS EMPTY")
        print(f'{button} pushed!')

def check_power(screen):
    match = r'\d+\^\d+'
    look_for_power = re.findall(match, screen)

    if look_for_power:
        for i in look_for_power:
            print('lalal ' + i)
            x = re.findall(r'\d+', i[0])
            a = f'{x[0]}'

            y = re.findall(r'\d+$', i)
            b = f'{y[0]}'

            ans = pow(float(a), float(b))

            screen = screen.replace(i, str(ans))
            print('new screen ' + screen)

    return screen


def main():
    app = QApplication(sys.argv)

    QDir.addSearchPath("icons", os.fspath(CURRENT_DIRECTORY / "icons"))
    icon = QIcon("icons:myicon1.png")
    assert not icon.isNull()

    window = MainWindow()
    window.setWindowIcon(icon)

    window.show()

    app.setStyleSheet("""
        QLineEdit {
            background-color: rgba(0, 0, 0, 0.4);
            font-family: 'Lucida Console', Monaco, monospace;
            font-size: 30px;
            font-weight: bold;
            border-radius: 50%;
            border-style: solid;
            border-width: 2px;
            border-color: #FFFFFF;
            color: white;
        }
        
        QLabel{
            background-color: rgba(0, 0, 0, 0.4);
            font-family: 'Lucida Console', Monaco, monospace;
            font-size: 30px;
            font-weight: bold;
            border-radius: 50%;
            border-style: solid;
            border-width: 2px;
            border-color: #FFFFFF;
            color: white;
        }
        
        QMainWindow {
            background-image: url("icons:myicon1.png");
        }
    """)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()